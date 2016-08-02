from django.test import TestCase
from django.core.urlresolvers import reverse

from user.models import CommuniqueUser

class CommuniqueUserAccessViewsTestCase(TestCase):
    """
    Test cases for the login and logout views.
    """
    def setUp(self):
        CommuniqueUser.objects.create_user('jon_snow', 'jonsnow@gmail.com',
            'p@55words')

    def test_login(self):
        """
        Test that login occurs on providing the right credentials.
        """
        self.assertFalse(self.client.login(username='dumb', password='secret'))
        self.assertTrue(self.client.login(username='jon_snow',
            password='p@55words'))

    def test_login_view_template(self):
        """
        Test that the right template is used to render the login page.
        """
        response = self.client.get(reverse('user_login'))
        self.assertTemplateUsed(response, 'user/login.html')

    def test_logout_view_template(self):
        """
        Test that the right template is used to render the logout page.
        """
        self.client.login(username='jon_snow', password='p@55words')
        response = self.client.get(reverse('user_logout'))
        self.assertTemplateUsed(response, 'user/logout.html')

class CommuniqueUserListViewTestCase(TestCase):
    """
    Test cases for the user list view.
    """
    def setUp(self):
        CommuniqueUser.objects.create_user('jon_snow', 'jonsnow@gmail.com', 'p@55words')
        self.client.login(username='jon_snow', password='p@55words')

    def test_template(self):
        """
        Test that the right template is used to render the account list page.
        """
        response = self.client.get(reverse('user_communique_user_list_view'))
        self.assertTemplateUsed(response, 'user/communique_user_list.html')

    def test_context_object(self):
        """
        Test that a context object is created and passed to the template of the
        account list view.
        """
        response = self.client.get(reverse('user_communique_user_list_view'))
        self.assertTrue(response.context['communique_user_list'])

class CommuniqueUserCreateViewTestCase(TestCase):
    """
    Test cases for the view to create users.
    """
    def setUp(self):
        CommuniqueUser.objects.create_user('jon_snow', 'jonsnow@gmail.com', 'p@55words')
        self.client.login(username='jon_snow', password='p@55words')

    def test_template(self):
        """
        Test that the right template is used to render the account create page.
        """
        response = self.client.get(reverse('user_communique_user_create_view'))
        self.assertTemplateUsed(response, 'user/communique_user_form.html')
