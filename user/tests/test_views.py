from django.test import TestCase
from django.contrib.auth.models import User

class UserViewsTestCase(TestCase):
    def setUp(self):
        User.objects.create_user('jon_snow', 'jonsnow@gmail.com', 'p@55words')

    def test_login(self):
        self.assertFalse(self.client.login(username='dumb', password='secret'))
        self.assertTrue(self.client.login(username='jon_snow',
            password='p@55words'))
