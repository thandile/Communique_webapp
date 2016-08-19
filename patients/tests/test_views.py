from django.core.urlresolvers import reverse

from communique.tests import ViewsTestCase

from patients.models import Patient


class PatientListViewTestCase(ViewsTestCase):
    """
    Test cases for the view that lists patients.
    """
    view_name = 'patients_patient_list'
    view_template_name = 'patients/patient_list.html'
    view_url = reverse(view_name)

    def test_active_user_access(self):
        self.only_active_user_access_test(self.view_url, self.view_template_name)


class PatientCreateViewTestCase(ViewsTestCase):
    """
    Test cases for the view that creates patients.
    """
    view_name = 'patients_patient_create'
    view_template_name = 'patients/patient_form.html'
    view_url = reverse(view_name)

    def test_active_user_access(self):
        self.only_active_user_access_test(self.view_url, self.view_template_name)


class PatientDetailViewTestCase(ViewsTestCase):
    """
    Test cases for the view that displays patient information.
    """
    view_name = 'patients_patient_detail'
    view_template_name = 'patients/patient_view.html'

    def test_active_user_access(self):
        patient = Patient.objects.create(first_name='Jon', last_name='Snow')
        self.only_active_user_access_test(patient.get_absolute_url(), self.view_template_name)


class PatientUpdateViewTestCase(ViewsTestCase):
    """
    Test cases for the update view for patient information.
    """
    view_name = 'patients_patient_update'
    view_template_name = 'patients/patient_update_form.html'

    def test_active_user_access(self):
        patient = Patient.objects.create(first_name='Jon', last_name='Snow')
        self.only_active_user_access_test(patient.get_update_url(), self.view_template_name)


class PatientDeleteViewTestCase(ViewsTestCase):
    """
    Test cases for the delete view of a patient.
    """
    view_name = 'patients_patient_delete'
    view_template_name = 'patients/patient_confirm_delete.html'

    def test_active_user_access(self):
        patient = Patient.objects.create(first_name='Jon', last_name='Snow')
        self.only_active_user_access_test(patient.get_delete_url(), self.view_template_name)