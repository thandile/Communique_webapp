from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from communique.views import (CommuniqueDeleteView, CommuniqueListView, CommuniqueDetailView, CommuniqueUpdateView,
                              CommuniqueCreateView, CommuniqueFormView)
from .models import Patient, Enrollment
from counselling_sessions.models import CounsellingSession
from appointments.models import Appointment
from medical.models import MedicalReport
from .forms import PatientAppointmentForm, PatientUploadFileForm, PatientRegimenForm
from admissions.models import Admission
from admissions.forms import AdmissionUpdateForm
from regimens.models import Regimen
from adverse.models import AdverseEvent
from patients.utils.utils_views import import_patients_from_file


class PatientListView(CommuniqueListView):
    """
    A view to list all patients that currently exist in the system.
    """
    model = Patient
    template_name = 'patients/patient_list.html'
    context_object_name = 'patient_list'


class PatientCreateView(CommuniqueCreateView):
    """
    A view to handle creation of patients.
    """
    model = Patient
    fields = ['last_name', 'other_names', 'identifier', 'reference_health_centre', 'birth_date', 'sex', 'location',
              'treatment_start_date', 'interim_outcome', 'contact_number']
    template_name = 'patients/patient_form.html'

    def form_valid(self, form):
        patient = form.save(commit=False)
        # update the created by and last modified by user markers
        patient.created_by = self.request.user
        patient.last_modified_by = self.request.user

        return super(PatientCreateView, self).form_valid(form)


class PatientDetailView(CommuniqueDetailView):
    """
    A view to display the details of a patient.
    """
    model = Patient
    template_name = 'patients/patient_view.html'
    context_object_name = 'patient'


class PatientUpdateView(CommuniqueUpdateView):
    """
    A view to handle updating patient information.
    """
    model = Patient
    fields = ['last_name', 'other_names', 'identifier', 'reference_health_centre', 'birth_date', 'sex', 'location',
              'treatment_start_date', 'interim_outcome', 'contact_number']
    template_name = 'patients/patient_update_form.html'
    context_object_name = 'patient'

    def form_valid(self, form):
        patient = form.save(commit=False)
        # update the last modified markers
        patient.last_modified_by = self.request.user

        return super(PatientUpdateView, self).form_valid(form)


class PatientDeleteView(CommuniqueDeleteView):
    """
    A view to handle the deletion of a patient.
    """
    model = Patient
    success_url = reverse_lazy('patients_patient_list')
    context_object_name = 'patient'
    template_name = 'patients/patient_confirm_delete.html'


class PatientImportView(SuccessMessageMixin, CommuniqueFormView):
    """
    A view to handle the importation of patients through an uploaded file.
    """
    template_name = 'patients/patient_import_form.html'
    form_class = PatientUploadFileForm
    success_url = reverse_lazy('patients_patient_list')
    success_message = 'The patients have successfully been added to the system.'

    def form_valid(self, form):
        # import the patients in the uploaded file
        uploaded_file = self.get_form_kwargs().get('files')['uploaded_file']
        import_patients_from_file(uploaded_file, self.request.user)
        return super(PatientImportView, self).form_valid(form)


class EnrollmentListView(CommuniqueListView):
    """
    A view to list all the enrollments that currently exist in the system.
    """
    model = Enrollment
    template_name = 'patients/enrollment_list.html'
    context_object_name = 'enrollment_list'


class EnrollmentCreateView(CommuniqueCreateView):
    """
    A view to handle creation of an enrollment.
    """
    model = Enrollment
    fields = ['patient', 'program', 'comment']
    template_name = 'patients/enrollment_form.html'

    def form_valid(self, form):
        enrollment = form.save(commit=False)
        # add user that has enrolled patient into program
        enrollment.enrolled_by = self.request.user

        return super(EnrollmentCreateView, self).form_valid(form)


class EnrollmentDetailView(CommuniqueDetailView):
    """
    A view to display details of an enrollment.
    """
    model = Enrollment
    template_name = 'patients/enrollment_view.html'
    context_object_name = 'enrollment'


class EnrollmentUpdateView(CommuniqueUpdateView):
    """
    A view to handle updating an enrollment.
    """
    model = Enrollment
    fields = ['is_active']
    template_name = 'patients/enrollment_update_form.html'
    context_object_name = 'enrollment'


class PatientModelCreateView(CommuniqueCreateView):
    """
    A view that handles the creation of another model from the Patients app.
    """
    def get_success_url(self):
        # on finalising the creation of the model, redirect to the patient details view
        patient = Patient.objects.get(pk=int(self.kwargs['patient_pk']))
        return patient.get_absolute_url()

    def get_context_data(self, **kwargs):
        context = super(PatientModelCreateView, self).get_context_data(**kwargs)
        patient = Patient.objects.get(pk=int(self.kwargs['patient_pk']))
        context['patient'] = patient
        return context


class PatientEnrollmentCreateView(PatientModelCreateView):
    """
    A view to create an enrollment for a defined patient.
    """
    model = Enrollment
    fields = ['program', 'comment']
    template_name = 'patients/patient_enrollment_form.html'

    def form_valid(self, form):
        # set the user that's made the enrollment and the patient whom it is for
        form.instance.enrolled_by = self.request.user
        patient = Patient.objects.get(pk=int(self.kwargs['patient_pk']))
        form.instance.patient = patient

        return super(PatientEnrollmentCreateView, self).form_valid(form)


class PatientSessionCreateView(PatientModelCreateView):
    """
    A view that handles creation of a session for a specific patient.
    """
    model = CounsellingSession
    fields = ['counselling_session_type', 'notes']
    template_name = 'patients/patient_session_form.html'

    def form_valid(self, form):
        # set the user adding the session and the patient whom it is for
        form.instance.created_by = self.request.user
        form.instance.last_modified_by = self.request.user
        patient = Patient.objects.get(pk=int(self.kwargs['patient_pk']))
        form.instance.patient = patient

        return super(PatientSessionCreateView, self).form_valid(form)


class PatientMedicalReportCreateView(PatientModelCreateView):
    """
    A view that handles creation of a medical report for a specific patient.
    """
    model = MedicalReport
    fields = ['title', 'report_type', 'notes']
    template_name = 'patients/patient_medical_report_form.html'

    def form_valid(self, form):
        # set the user adding the medical report and the patient whom it is for
        form.instance.created_by = self.request.user
        form.instance.last_modified_by = self.request.user
        patient = Patient.objects.get(pk=int(self.kwargs['patient_pk']))
        form.instance.patient = patient

        return super(PatientMedicalReportCreateView, self).form_valid(form)


class PatientAppointmentCreateView(PatientModelCreateView):
    """
    A view that handles creation of an appointment for a specific patient.
    """
    model = Appointment
    form_class = PatientAppointmentForm
    template_name = 'patients/patient_appointment_form.html'

    def form_valid(self, form):
        # set the user adding the appointment and the patient whom it is for
        form.instance.created_by = self.request.user
        form.instance.last_modified_by = self.request.user

        if not form.instance.owner:
            form.instance.owner = self.request.user

        patient = Patient.objects.get(pk=int(self.kwargs['patient_pk']))
        form.instance.patient = patient

        return super(PatientAppointmentCreateView, self).form_valid(form)


class PatientAdmissionCreateView(PatientModelCreateView):
    """
    A view that handles admission for a specific patient.
    """
    model = Admission
    form_class = AdmissionUpdateForm
    template_name = 'patients/patient_admission_form.html'

    def form_valid(self, form):
        # set the created by and last modified by fields
        form.instance.created_by = self.request.user
        form.instance.last_modified_by = self.request.user

        patient = Patient.objects.get(pk=int(self.kwargs['patient_pk']))
        form.instance.patient = patient

        return super(PatientAdmissionCreateView, self).form_valid(form)


class PatientRegimenCreateView(PatientModelCreateView):
    """
    A view that handles adding a regimen for a specific patient.
    """
    model = Regimen
    form_class = PatientRegimenForm
    template_name = 'patients/patient_regimen_form.html'

    def form_valid(self, form):
        # set the created by and last modified by fields
        form.instance.created_by = self.request.user
        form.instance.last_modified_by = self.request.user

        patient = Patient.objects.get(pk=int(self.kwargs['patient_pk']))
        form.instance.patient = patient

        return super(PatientRegimenCreateView, self).form_valid(form)


class PatientAdverseEventCreateView(PatientModelCreateView):
    """
    A view that handles adding an adverse event for a specific patient.
    """
    model = AdverseEvent
    fields = ['adverse_event_type', 'event_date', 'notes']
    template_name = 'patients/patient_adverse_event_form.html'

    def form_valid(self, form):
        # set teh created by and last modified by fields
        form.instance.created_by = self.request.user
        form.instance.last_modified_by = self.request.user

        patient = Patient.objects.get(pk=int(self.kwargs['patient_pk']))
        form.instance.patient = patient

        return super(PatientAdverseEventCreateView, self).form_valid(form)

