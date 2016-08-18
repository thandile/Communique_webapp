"""
This file contains test cases for views of the programs app.
"""
from django.core.urlresolvers import reverse

from communique.tests import ViewsTestCase

from programs.models import Program


class ProgramListViewTestCase(ViewsTestCase):
    """
    Test cases for the view that lists programs.
    """
    view_name = 'programs_program_list'
    view_template_name = 'programs/program_list.html'
    view_url = reverse(view_name)

    def test_active_user_access(self):
        self.only_active_user_access_test(self.view_url, self.view_template_name)


class ProgramCreateViewTestCase(ViewsTestCase):
    """
    Test cases for view to create a program.
    """
    view_name = 'programs_program_create'
    view_template_name = 'programs/program_form.html'
    view_url = reverse(view_name)

    def test_active_user_access(self):
        self.only_active_user_access_test(self.view_url, self.view_template_name)


class ProgramDetailViewTestCase(ViewsTestCase):
    """
    Test cases for view to show the details of a program.
    """
    view_name = 'programs_program_detail'
    view_template_name = 'programs/program_view.html'

    def test_active_user_access(self):
        program = Program.objects.create(name='Sample Program', description='Sample Description')
        self.only_active_user_access_test(program.get_absolute_url(), self.view_template_name)


class ProgramUpdateViewTestCase(ViewsTestCase):
    """
    Test cases for view to update the details of a program.
    """
    view_name = 'programs_program_update'
    view_template_name = 'programs/program_update_form.html'

    def test_active_user_access(self):
        program = Program.objects.create(name='Sample Program', description='Sample Description')
        self.only_active_user_access_test(program.get_update_url(), self.view_template_name)

