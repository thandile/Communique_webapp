"""
Contains test cases for the models of the user app.
"""
from django.test import TestCase
from django.core.urlresolvers import reverse

from user.models import *

class CommuniqueUserTestCase(TestCase):
    """
    Test cases for the CommuniqueUser model.
    """
    def setUp(self):
        CommuniqueUser.objects.create_superuser('jon_snow', 'jonsnow@gmail.com',
            'p@55words')

    def test_get_absolute_url(self):
        """
        Tests that the right url path is returned to obtain the details of a
        Communiqué user.
        """
        user = CommuniqueUser.objects.get(username='jon_snow')
        self.assertEqual(user.get_absolute_url(), '/user/communique-users/' +
            str(user.pk) + '/')

    def test_get_update_url(self):
        """
        Tests that the right url path is returned to update a Communiqué user.
        """
        user = CommuniqueUser.objects.get(username='jon_snow')
        self.assertEqual(user.get_update_url(), '/user/communique-users/'
            + str(user.pk) + '/update/')

    def test_get_set_password_url(self):
        """
        Tests that the right url path is returned to set the password of a
        Communiqué user.
        """
        user = CommuniqueUser.objects.get(username='jon_snow')
        self.assertEqual(user.get_set_password_url(), '/user/communique-users/'
            + str(user.pk) + '/set-password/')

class ProfileTestCase(TestCase):
    """
    Test cases for the Profile model.
    """
    def setUp(self):
        Profile.objects.create_superuser('jon_snow', 'jonsnow@gmail.com',
            'p@55words')

    def test_get_absolute_url(self):
        """
        Tests that the right url path is returned to obtain the details of a
        Profile.
        """
        profile = Profile.objects.get(username='jon_snow')
        self.assertEqual(profile.get_absolute_url(), '/user/profile/' +
            str(profile.pk) + '/')

    def test_get_update_url(self):
        """
        Tests that the right url path is returned to update the details of a
        Profile.
        """
        profile = Profile.objects.get(username='jon_snow')
        self.assertEqual(profile.get_update_url(), '/user/profile/' + str(profile.pk) + '/update/')
