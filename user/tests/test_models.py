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
        Communique user.
        """
        user = CommuniqueUser.objects.get(username='jon_snow')
        self.assertEqual(user.get_absolute_url(), '/user/communique-users/' +
            str(user.pk) + '/')
