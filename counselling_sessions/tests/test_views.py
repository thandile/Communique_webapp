from django.core.urlresolvers import reverse

from communique.tests import ViewsTestCase


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