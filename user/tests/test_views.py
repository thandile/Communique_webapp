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
        CommuniqueUser.objects.create_user('regular_user',
            'regularuser@gmail.com', 'p@55words')
        CommuniqueUser.objects.create_superuser('super_user',
            'superuser@gmail.com', 'p@55words')

    def test_template(self):
        """
        Tests that the right template is used to render the user list page.
        """
        self.client.login(username='super_user', password='p@55words')
        response = self.client.get(reverse('user_communique_user_list'))
        self.assertTemplateUsed(response, 'user/communique_user_list.html')

    def test_only_superuser_access(self):
        """
        Tests that only a superuser can access this view.

        If the user is not a superuser, he or she is redirected to the login
        page.
        """
        super_user = CommuniqueUser.objects.get(username='super_user')
        self.assertTrue(super_user.is_superuser)
        self.client.force_login(super_user)
        response = self.client.get(reverse('user_communique_user_list'),
            follow=True)
        self.assertTemplateUsed(response, 'user/communique_user_list.html')
        self.client.logout()

        regular_user = CommuniqueUser.objects.get(username='regular_user')
        self.assertFalse(regular_user.is_superuser)
        self.client.force_login(regular_user)
        response = self.client.get(reverse('user_communique_user_list'),
            follow=True)
        self.assertTemplateUsed(response, 'user/login.html')

    def test_context_object(self):
        """
        Test that a context object is created and passed to the template of the
        account list view.
        """
        self.client.login(username='super_user', password='p@55words')
        response = self.client.get(reverse('user_communique_user_list'))
        self.assertTrue(response.context['communique_user_list'])

class CommuniqueUserCreateViewTestCase(TestCase):
    """
    Test cases for the view to create users.
    """
    def setUp(self):
        CommuniqueUser.objects.create_superuser('super_user', 'superuser@gmail.com',
            'p@55words')
        CommuniqueUser.objects.create_user('regular_user', 'regularuser@gmail.com',
            'p@55words')

    def test_template(self):
        """
        Tests that the right template is used to render the account create page.
        """
        self.client.login(username='super_user', password='p@55words')
        response = self.client.get(reverse('user_communique_user_create'))
        self.assertTemplateUsed(response, 'user/communique_user_form.html')

    def test_only_superuser_access(self):
        """
        Tests that only a superuser can access this view.

        If the user is not a superuser, he/she is redirected to the login page.
        """
        regular_user = CommuniqueUser.objects.get(username='regular_user')
        self.assertFalse(regular_user.is_superuser)
        self.client.force_login(regular_user)
        response = self.client.get(reverse('user_communique_user_create'),
            follow=True)
        self.assertTemplateUsed(response, 'user/login.html')
        self.client.logout()

        super_user = CommuniqueUser.objects.get(username='super_user')
        self.assertTrue(super_user.is_superuser)
        self.client.force_login(super_user)
        response = self.client.get(reverse('user_communique_user_create'),
            follow=True)
        self.assertTemplateUsed(response, 'user/communique_user_form.html')

class CommuniqueUserDetailViewTestCase(TestCase):
    """
    Test cases for the view to see user details.
    """
    def setUp(self):
        CommuniqueUser.objects.create_superuser('super_user',
            'superuser@gmail.com', 'p@55words')
        CommuniqueUser.objects.create_user('regular_user', 'superuser@gmail.com',
            'p@55words')

    def test_template(self):
        """
        Tests that the right template is used to render user detail view page.
        """
        self.client.login(username='super_user', password='p@55words')
        response = self.client.get(reverse('user_communique_user_detail',
            kwargs={'pk':1}))
        self.assertTemplateUsed(response, 'user/communique_user_view.html')

    def test_only_superuser_access(self):
        """
        Tests that only a superuser can access this view.
        If the user is not a superuser, he/she is redirected to the login page.
        """
        regular_user = CommuniqueUser.objects.get(username='regular_user')
        self.assertFalse(regular_user.is_superuser)
        self.client.force_login(regular_user)
        response = self.client.get(reverse('user_communique_user_detail',
            kwargs={'pk':regular_user.id}), follow=True)
        self.assertTemplateUsed(response, 'user/login.html')
        self.client.logout()

        super_user = CommuniqueUser.objects.get(username='super_user')
        self.assertTrue(super_user.is_superuser)
        self.client.force_login(super_user)
        response = self.client.get(reverse('user_communique_user_detail',
            kwargs={'pk':super_user.id}), follow=True)
        self.assertTemplateUsed(response, 'user/communique_user_view.html')
