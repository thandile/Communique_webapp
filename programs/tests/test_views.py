"""
This file contains test cases for views of the programs app.
"""
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from programs.models import Program


class ProgramsViewsTestCase(TestCase):
    def setUp(self):
        """
        Creates an active and inactive user to be used throughout testing.
        """
        # by default, a created user is active
        User.objects.create_user(username='active_user', email='activeuser@gmail.com', password='p@55words')
        inactive_user = User.objects.create_user(username='inactive_user', email='inactiveuser@gmail.com',
                                                 password='p@55words')
        inactive_user.is_active = False
        inactive_user.save()

    def only_active_user_access_test(self, view_url, template_name):
        """
        Tests that only active users have access to this view.
        :param view_url: The url of view being tested.
        :param template_name: The name of the template for the view being tested.
        """
        active_user = User.objects.get(username='active_user')
        self.assertTrue(active_user.is_active)
        self.client.force_login(active_user)
        response = self.client.get(view_url, follow=True)
        self.assertTemplateUsed(response, template_name)
        self.client.logout()

        inactive_user = User.objects.get(username='inactive_user')
        self.assertFalse(inactive_user.is_active)
        self.client.force_login(inactive_user)
        response = self.client.get(view_url, follow=True)
        self.assertTemplateUsed(response, 'user/login.html')


class ProgramListViewTestCase(ProgramsViewsTestCase):
    """
    Test cases for the view that lists programs.
    """
    view_name = 'programs_program_list'
    view_template_name = 'programs/program_list.html'
    view_url = reverse(view_name)

    def test_active_user_access(self):
        self.only_active_user_access_test(self.view_url, self.view_template_name)


class ProgramCreateViewTestCase(ProgramsViewsTestCase):
    """
    Test cases for view to create a program.
    """
    view_name = 'programs_program_create'
    view_template_name = 'programs/program_form.html'
    view_url = reverse(view_name)

    def test_active_user_access(self):
        self.only_active_user_access_test(self.view_url, self.view_template_name)


class ProgramDetailViewTestCase(ProgramsViewsTestCase):
    """
    Test cases for view to show the details of a program.
    """
    view_name = 'programs_program_detail'
    view_template_name = 'programs/program_view.html'

    def test_active_user_access(self):
        program = Program.objects.create(name='Sample Program', description='Sample Description')
        self.only_active_user_access_test(program.get_absolute_url(), self.view_template_name)


class ProgramUpdateViewTestCase(ProgramsViewsTestCase):
    """
    Test cases for view to update the details of a program.
    """
    view_name = 'programs_program_update'
    view_template_name = 'programs/program_update_form.html'

    def test_active_user_access(self):
        program = Program.objects.create(name='Sample Program', description='Sample Description')
        self.only_active_user_access_test(program.get_update_url(), self.view_template_name)

