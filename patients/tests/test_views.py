from django.core.urlresolvers import reverse

from communique.tests import ViewsTestCase


class PatientListViewTestCase(ViewsTestCase):
    """
    Test cases for the view that lists patients.
    """
    view_name = 'patients_patient_list'
    view_template_name = 'patients/patient_list.html'
    view_url = reverse(view_name)

    def test_active_user_access(self):
        self.only_active_user_access_test(self.view_url, self.view_template_name)


