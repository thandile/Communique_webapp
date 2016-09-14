from django.core.urlresolvers import reverse_lazy

from .models import *
from communique.views import (CommuniqueDeleteView, CommuniqueListView, CommuniqueDetailView, CommuniqueUpdateView,
                              CommuniqueCreateView)


class CounsellingSessionTypeListView(CommuniqueListView):
    """
    A view that retrieves all the available session types.
    """
    model = CounsellingSessionType
    template_name = 'counselling_sessions/counselling_session_type_list.html'
    context_object_name = 'counselling_session_type_list'


class CounsellingSessionTypeCreateView(CommuniqueCreateView):
    """
    A view that handles creation of a session type.
    """
    model = CounsellingSessionType
    template_name = 'counselling_sessions/counselling_session_type_form.html'
    fields = ['name', 'description']

    def form_valid(self, form):
        counselling_session_type = form.save(commit=False)
        # update the created by and last modified by fields
        counselling_session_type.created_by = self.request.user
        counselling_session_type.last_modified_by = self.request.user

        return super(CounsellingSessionTypeCreateView, self).form_valid(form)


class CounsellingSessionTypeDetailView(CommuniqueDetailView):
    """
    A view that handles displaying details of a session type.
    """
    model = CounsellingSessionType
    template_name = 'counselling_sessions/counselling_session_type_view.html'
    context_object_name = 'counselling_session_type'


class CounsellingSessionTypeUpdateView(CommuniqueUpdateView):
    """
    A view that handles updating of a session type.
    """
    model = CounsellingSessionType
    fields = ['name', 'description']
    template_name = 'counselling_sessions/counselling_session_type_update_form.html'
    context_object_name = 'counselling_session_type'

    def form_valid(self, form):
        session_type = form.save(commit=False)
        # update the last modified field
        session_type.last_modified_by = self.request.user

        return super(CounsellingSessionTypeUpdateView, self).form_valid(form)


class CounsellingSessionTypeDeleteView(CommuniqueDeleteView):
    """
    A view that handles the deletion of a session type.
    """
    model = CounsellingSessionType
    success_url = reverse_lazy('counselling_sessions_type_list')
    context_object_name = 'counselling_session_type'
    template_name = 'counselling_sessions/counselling_session_type_confirm_delete.html'


class CounsellingSessionListView(CommuniqueListView):
    """
    A view that retrieves all available sessions.
    """
    model = CounsellingSession
    template_name = 'counselling_sessions/counselling_session_list.html'
    context_object_name = 'counselling_session_list'


class CounsellingSessionCreateView(CommuniqueCreateView):
    """
    A view that handles creation of a session.
    """
    model = CounsellingSession
    template_name = 'counselling_sessions/counselling_session_form.html'
    fields = ['counselling_session_type', 'patient', 'notes']

    def form_valid(self, form):
        counselling_session = form.save(commit=False)
        # update the created by and last modified by fields
        counselling_session.created_by = self.request.user
        counselling_session.last_modified_by = self.request.user

        return super(CounsellingSessionCreateView, self).form_valid(form)


class CounsellingSessionDetailView(CommuniqueDetailView):
    """
    A view that handles displaying details of a session.
    """
    model = CounsellingSession
    template_name = 'counselling_sessions/counselling_session_view.html'
    context_object_name = 'counselling_session'


class CounsellingSessionUpdateView(CommuniqueUpdateView):
    """
    A view that handles updating a session.
    """
    model = CounsellingSession
    fields = ['notes']
    template_name = 'counselling_sessions/counselling_session_update_form.html'
    context_object_name = 'counselling_session'

    def form_valid(self, form):
        counselling_session = form.save(commit=False)
        # update the last modified field
        counselling_session.last_modified_by = self.request.user

        return super(CounsellingSessionUpdateView, self).form_valid(form)


class CounsellingSessionDeleteView(CommuniqueDeleteView):
    """
    A view that handles the deletion of a session.
    """
    model = CounsellingSession
    success_url = reverse_lazy('counselling_sessions_session_list')
    context_object_name = 'counselling_session'
    template_name = 'counselling_sessions/counselling_session_confirm_delete.html'
