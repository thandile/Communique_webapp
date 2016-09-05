from django.core.urlresolvers import reverse

from communique.tests import ViewsTestCase

from counselling_sessions.models import CounsellingSessionType


class CounsellingSessionTypeListViewTestCase(ViewsTestCase):
    """
    Test cases for the view that lists counselling session types.
    """
    view_name = 'counselling_sessions_type_list'
    view_template_name = 'counselling_sessions/counselling_session_type_list.html'
    view_url = reverse(view_name)

    def test_active_user_access(self):
        self.only_active_user_access_test(self.view_url, self.view_template_name)


class CounsellingSessionTypeCreateViewTestCase(ViewsTestCase):
    """
    Test cases for the view to create a new session type.
    """
    view_name = 'counselling_sessions_type_create'
    view_template_name = 'counselling_sessions/counselling_session_type_form.html'
    view_url = reverse(view_name)

    def test_active_user_access(self):
        self.only_active_user_access_test(self.view_url, self.view_template_name)


class CounsellingSessionTypeDetailViewTestCase(ViewsTestCase):
    """
    Test cases for the view to display session type information.
    """
    view_name = 'counselling_sessions_type_detail'
    view_template_name = 'counselling_sessions/counselling_session_type_view.html'

    def test_active_user_access(self):
        session_type = CounsellingSessionType.objects.create(name='Dummy Type')
        self.only_active_user_access_test(session_type.get_absolute_url(), self.view_template_name)


class CounsellingSessionTypeUpdateViewTestCase(ViewsTestCase):
    """
    Test cases for the view to update a session type.
    """
    view_name = 'counselling_sessions_type_update'
    view_template_name = 'counselling_sessions/counselling_session_type_update_form.html'

    def test_active_user_access(self):
        session_type = CounsellingSessionType.objects.create(name='Dummy type')
        self.only_active_user_access_test(session_type.get_update_url(), self.view_template_name)


class CounsellingSessionTypeDeleteViewTestCase(ViewsTestCase):
    """
    Test cases for the view to delete a session type.
    """
    view_name = 'counselling_sessions_type_delete'
    view_template_name = 'counselling_sessions/counselling_session_type_confirm_delete.html'

    def test_active_user_access(self):
        session_type = CounsellingSessionType.objects.create(name='Dummy type')
        self.only_active_user_access_test(session_type.get_delete_url(), self.view_template_name)


class CounsellingSessionListViewTestCase(ViewsTestCase):
    """
    Test cases for the view that lists counselling sessions.
    """
    view_name = 'counselling_sessions_session_list'
    view_template_name = 'counselling_sessions/counselling_session_list.html'
    view_url = reverse(view_name)

    def test_active_user_access(self):
        self.only_active_user_access_test(self.view_url, self.view_template_name)


class CounsellingSessionCreateViewTestCase(ViewsTestCase):
    """
    Test cases for the view to add a session.
    """
    view_name = 'counselling_sessions_session_create'
    view_template_name = 'counselling_sessions/counselling_session_form.html'
    view_url = reverse(view_name)

    def test_active_user_access(self):
        self.only_active_user_access_test(self.view_url, self.view_template_name)
