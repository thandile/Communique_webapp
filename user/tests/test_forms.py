from django.test import TestCase

from user.forms import *
from user.models import CommuniqueUser

class CommuniqueUserCreationFormTestCase(TestCase):
    """
    Test cases for the Communique user creation form.
    """

    def test_minimum_data_requirements(self):
        """
        Tests the minimum requirements for the user creation form which are:
        username and password.
        """
        form = CommuniqueUserCreationForm()
        self.assertFalse(form.is_bound)
        self.assertFalse(form.is_valid())

        data = {'username':'jon_snow', 'password1':'p@55words',
            'password2':'p@55words'}
        form = CommuniqueUserCreationForm(data)
        self.assertTrue(form.is_bound)
        self.assertTrue(form.is_valid())

        user = form.save()
        self.assertEqual(user.username, 'jon_snow')

    def test_all_data_requirements(self):
        """
        Tests that the expected data (username, last name, first name,
        is_superuser, email and password) are all accepted by the user creation
        form.
        """
        data = {'first_name':'Jon', 'last_name':'Snow', 'username':'jon_snow',
            'is_superuser':True, 'email':'jonsnow@gmail.com',
            'password1':'p@55words', 'password2':'p@55words'}
        form = CommuniqueUserCreationForm(data)
        self.assertTrue(form.is_bound)
        self.assertTrue(form.is_valid())

        user = form.save()
        self.assertEqual(user.first_name, 'Jon')
        self.assertEqual(user.last_name, 'Snow')
        self.assertEqual(user.username, 'jon_snow')
        self.assertTrue(user.is_superuser)
        self.assertEqual(user.email, 'jonsnow@gmail.com')

    def test_username_uniqueness(self):
        """
        Tests that the user creation form to show that username must be unique.
        """
        CommuniqueUser.objects.create_user('jon_snow', 'jonsnow@gmail.com',
            'p@55words')

        data = {'username':'jon_snow', 'password1':'B@5tards',
            'password2':'B@5tards'}
        form = CommuniqueUserCreationForm(data)
        self.assertTrue(form.is_bound)
        self.assertFalse(form.is_valid())
