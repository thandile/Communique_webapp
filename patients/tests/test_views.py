from django.core.urlresolvers import reverse

from communique.tests import ViewsTestCase

from patients.models import Patient, Enrollment
from programs.models import Program


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


class EnrollmentListViewTestCase(ViewsTestCase):
    """
    Test cases for the enrollment list view.
    """
    view_name = 'patients_enrollment_list'
    view_template_name = 'patients/enrollment_list.html'
    view_url = reverse(view_name)

    def test_active_user_access(self):
        self.only_active_user_access_test(self.view_url, self.view_template_name)


class EnrollmentCreateViewTestCase(ViewsTestCase):
    """
    Test cases for the enrollment create view.
    """
    view_name = 'patients_enrollment_create'
    view_template_name = 'patients/enrollment_form.html'
    view_url = reverse(view_name)

    def test_active_user_access(self):
        self.only_active_user_access_test(self.view_url, self.view_template_name)


class EnrollmentDetailViewTestCase(ViewsTestCase):
    """
    Test cases for the enrollment detail view.
    """
    view_name = 'patients_enrollment_detail'
    view_template_name = 'patients/enrollment_view.html'

    def test_active_user_access(self):
        patient = Patient.objects.create(first_name='Jon', last_name='Snow')
        program = Program.objects.create(name='Sample', description='sample text')
        enrollment = Enrollment.objects.create(patient=patient, program=program, comment='No comment')
        self.only_active_user_access_test(enrollment.get_absolute_url(), self.view_template_name)


class EnrollmentUpdateViewTestCase(ViewsTestCase):
    """
    Test cases for the enrollment update view.
    """
    view_name = 'patients_enrollment_update'
    view_template_name = 'patients/enrollment_update_form.html'

    def test_active_user_access(self):
        patient = Patient.objects.create(first_name='Jon', last_name='Snow')
        program = Program.objects.create(name='Sample', description='sample text')
        enrollment = Enrollment.objects.create(patient=patient, program=program, comment='No comment')
        self.only_active_user_access_test(enrollment.get_update_url(), self.view_template_name)


class PatientEnrollmentCreateViewTestCase(ViewsTestCase):
    """
    Test cases for the view to create an enrollment for a specific patient.
    """
    view_name = 'patients_patient_enroll_create'
    view_template_name = 'patients/patient_enrollment_form.html'

    def test_active_user_access(self):
        patient = Patient.objects.create(first_name='Jon', last_name='Snow')
        view_url = reverse(self.view_name, kwargs={'patient_pk':patient.pk})
        self.only_active_user_access_test(view_url, self.view_template_name)


class PatientSessionCreateViewTestCase(ViewsTestCase):
    """
    Test cases for the view to create a session for a specific patient.
    """
    view_name = 'patients_patient_session_create'
    view_template_name = 'patients/patient_session_form.html'

    def test_active_user_access(self):
        patient = Patient.objects.create(first_name='Jon', last_name='Snow')
        view_url = reverse(self.view_name, kwargs={'patient_pk':patient.pk})
        self.only_active_user_access_test(view_url, self.view_template_name)


class PatientMedicalReportCreateViewTestCase(ViewsTestCase):
    """
    Test cases for the view to create a medical report for a specific patient.
    """
    view_name = 'patients_patient_medical_report_create'
    view_template_name = 'patients/patient_medical_report_form.html'

    def test_active_user_access(self):
        patient = Patient.objects.create(first_name='Jon', last_name='Snow')
        view_url = reverse(self.view_name, kwargs={'patient_pk':patient.pk})
        self.only_active_user_access_test(view_url, self.view_template_name)


class PatientAppointmentCreateViewTestCase(ViewsTestCase):
    """
    Test cases for the view to create an appointment for a specific patient.
    """
    view_name = 'patients_patient_appointment_create'
    view_template_name = 'patients/patient_appointment_form.html'

    def test_active_user_access(self):
        patient = Patient.objects.create(first_name='Jon', last_name='Snow')
        view_url = reverse(self.view_name, kwargs={'patient_pk':patient.pk})
        self.only_active_user_access_test(view_url, self.view_template_name)