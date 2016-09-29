from django.core.urlresolvers import reverse_lazy

from .models import MedicalReport, MedicalReportType
from communique.views import (CommuniqueDeleteView, CommuniqueListView, CommuniqueDetailView, CommuniqueUpdateView,
                              CommuniqueCreateView)


class MedicalReportTypeListView(CommuniqueListView):
    """
    A view that retrieves all available medical report types.
    """
    model = MedicalReportType
    template_name = 'medical/medical_report_type_list.html'
    context_object_name = 'medical_report_type_list'


class MedicalReportTypeCreateView(CommuniqueCreateView):
    """
    A view that handles creation of a report type.
    """
    model = MedicalReportType
    template_name = 'medical/medical_report_type_form.html'
    fields = ['name', 'description']

    def form_valid(self, form):
        # fill the created by and modified by fields
        form.instance.created_by = self.request.user
        form.instance.last_modified_by = self.request.user

        return super(MedicalReportTypeCreateView, self).form_valid(form)


class MedicalReportTypeDetailView(CommuniqueDetailView):
    """
    A view that handles displaying details of a report type.
    """
    model = MedicalReportType
    template_name = 'medical/medical_report_type_view.html'
    context_object_name = 'medical_report_type'


class MedicalReportTypeUpdateView(CommuniqueUpdateView):
    """
    A view that handles updating the details of a report type.
    """
    model = MedicalReportType
    fields = ['name', 'description']
    template_name = 'medical/medical_report_type_update_form.html'
    context_object_name = 'medical_report_type'

    def form_valid(self, form):
        # update the modified by fields
        form.instance.last_modified_by = self.request.user

        return super(MedicalReportTypeUpdateView, self).form_valid(form)


class MedicalReportTypeDeleteView(CommuniqueDeleteView):
    """
    This view handles the deletion of a report type.
    """
    model = MedicalReportType
    success_url = reverse_lazy('medical_report_type_list')
    context_object_name = 'medical_report_type'
    template_name = 'medical/medical_report_type_confirm_delete.html'


class MedicalReportListView(CommuniqueListView):
    """
    A view that retrieves all available medical reports.
    """
    model = MedicalReport
    template_name = 'medical/medical_report_list.html'
    context_object_name = 'medical_report_list'


class MedicalReportCreateView(CommuniqueCreateView):
    """
    A view that handles the creation of a medical report.
    """
    model = MedicalReport
    template_name = 'medical/medical_report_form.html'
    fields = ['title', 'report_type', 'patient', 'notes']

    def form_valid(self, form):
        # set the created by and modified by fields
        form.instance.created_by = self.request.user
        form.instance.last_modified_by = self.request.user

        return super(MedicalReportCreateView, self).form_valid(form)


class MedicalReportDetailView(CommuniqueDetailView):
    """
    A view that handles displaying details of a medical report.
    """
    model = MedicalReport
    template_name = 'medical/medical_report_view.html'
    context_object_name = 'medical_report'


class MedicalReportUpdateView(CommuniqueUpdateView):
    """
    A view that handles updating a medical report.
    """
    model = MedicalReport
    template_name = 'medical/medical_report_update_form.html'
    fields = ['title', 'report_type', 'notes']
    context_object_name = 'medical_report'

    def form_valid(self, form):
        # set the modified fields
        form.instance.last_modified_by = self.request.user

        return super(MedicalReportUpdateView, self).form_valid(form)


class MedicalReportDeleteView(CommuniqueDeleteView):
    """
    A view that handles the deletion of a medical report.
    """
    model = MedicalReport
    success_url = reverse_lazy('medical_report_list')
    context_object_name = 'medical_report'
    template_name = 'medical/medical_report_confirm_delete.html'
