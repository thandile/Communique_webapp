from django.core.urlresolvers import reverse_lazy

from .models import Program
from communique.views import (CommuniqueDeleteView, CommuniqueListView, CommuniqueDetailView, CommuniqueUpdateView,
                              CommuniqueCreateView)


class ProgramListView(CommuniqueListView):
    """
    A view to list all programs of the system.
    """
    model = Program
    template_name = "programs/program_list.html"
    context_object_name = 'program_list'


class ProgramCreateView(CommuniqueCreateView):
    """
    A view to handle creation of a Program by displaying the form and handling the post request.
    """
    model = Program
    fields = ['name', 'description', 'is_open']
    template_name = 'programs/program_form.html'

    def form_valid(self, form):
        program = form.save(commit=False)
        # update the created by and last modified by markers
        program.created_by = self.request.user
        program.last_modified_by = self.request.user

        return super(ProgramCreateView, self).form_valid(form)


class ProgramDetailView(CommuniqueDetailView):
    """
    A view to display the details of a Program.
    """
    model = Program
    template_name = 'programs/program_view.html'
    context_object_name = 'program'


class ProgramUpdateView(CommuniqueUpdateView):
    """
    A view to update the details of a Program.
    """
    model = Program
    fields = ['name', 'description', 'is_open']
    template_name = 'programs/program_update_form.html'
    context_object_name = 'program'

    def form_valid(self, form):
        program = form.save(commit=False)
        # update the last modified by markers
        program.last_modified_by = self.request.user

        return super(ProgramUpdateView, self).form_valid(form)


class ProgramDeleteView(CommuniqueDeleteView):
    """
    A view to handle deletion of a program.
    """
    model = Program
    success_url = reverse_lazy('programs_program_list')
    context_object_name = 'program'
    template_name = 'programs/program_confirm_delete.html'
