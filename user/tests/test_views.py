from django.test import TestCase
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class UserViewsTestCase(TestCase):
    def setUp(self):
        User.objects.create_user('jon_snow', 'jonsnow@gmail.com', 'p@55words')

    def test_login(self):
        self.assertFalse(self.client.login(username='dumb', password='secret'))
        self.assertTrue(self.client.login(username='jon_snow',
            password='p@55words'))

    def test_login_view_template(self):
        response = self.client.get(reverse('user_login'))
        self.assertTemplateUsed(response, 'user/login.html')

    def test_logout_view_template(self):
        self.client.login(username='jon_snow', password='p@55words')
        response = self.client.get(reverse('user_logout'))
        self.assertTemplateUsed(response, 'user/logout.html')
