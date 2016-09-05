from django.core.urlresolvers import reverse

from communique.tests import ViewsTestCase

from counselling_sessions.models import CounsellingSessionType, CounsellingSession
from patients.models import Patient


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
    view_template_name = 'counselling_sessions/counselling_session_type_view.html'

    def test_active_user_access(self):
        session_type = CounsellingSessionType.objects.create(name='Dummy Type')
        self.only_active_user_access_test(session_type.get_absolute_url(), self.view_template_name)


class CounsellingSessionTypeUpdateViewTestCase(ViewsTestCase):
    """
    Test cases for the view to update a session type.
    """
    view_template_name = 'counselling_sessions/counselling_session_type_update_form.html'

    def test_active_user_access(self):
        session_type = CounsellingSessionType.objects.create(name='Dummy type')
        self.only_active_user_access_test(session_type.get_update_url(), self.view_template_name)


class CounsellingSessionTypeDeleteViewTestCase(ViewsTestCase):
    """
    Test cases for the view to delete a session type.
    """
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


class CounsellingSessionDetailViewTestCase(ViewsTestCase):
    """
    Test cases for the view to display a session.
    """
    view_template_name = 'counselling_sessions/counselling_session_view.html'

    def test_active_user_access(self):
        session_type = CounsellingSessionType.objects.create(name='dummy type')
        patient = Patient.objects.create(first_name='Jon', last_name='Snow')
        counselling_session = CounsellingSession.objects.create(patient=patient, counselling_session_type=session_type)
        self.only_active_user_access_test(counselling_session.get_absolute_url(), self.view_template_name)


class CounsellingSessionUpdateViewTestCase(ViewsTestCase):
    """
    Test cases for the view to update a session.
    """
    view_template_name = 'counselling_sessions/counselling_session_update_form.html'

    def test_active_user_access(self):
        session_type = CounsellingSessionType.objects.create(name='dummy type')
        patient = Patient.objects.create(first_name='Jon', last_name='Snow')
        counselling_session = CounsellingSession.objects.create(patient=patient, counselling_session_type=session_type)
        self.only_active_user_access_test(counselling_session.get_update_url(), self.view_template_name)