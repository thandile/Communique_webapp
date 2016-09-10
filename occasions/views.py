from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.urlresolvers import reverse_lazy

from .models import Event
from .forms import EventForm


class EventCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    """
    A view that handles creation of an event.

    This view is only available to users that are logged in and are marked as active in the system.
    """
    model = Event
    form_class = EventForm
    template_name = 'occasions/event_form.html'

    def form_valid(self, form):
        # fill the creator and last modified fields
        form.instance.created_by = self.request.user
        form.instance.last_modified_by = self.request.user

        return super(EventCreateView, self).form_valid(form)

    def test_func(self):
        """
        Checks whether the user is marked active
        :return: True if user is active, false otherwise
        """
        return self.request.user.is_active


class EventDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    """
    A view that handles displaying event details.

    This view is only available to users that are logged in and are marked as active in the system.
    """
    model = Event
    template_name = 'occasions/event_view.html'
    context_object_name = 'event'

    def test_func(self):
        """
        Checks whether the user is marked active
        :return: True if user is active, false otherwise
        """
        return self.request.user.is_active


class EventUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    A view that handles updating an event.

    This view is only available to users that are logged in and are marked as active in the system.
    """
    model = Event
    form_class = EventForm
    template_name = 'occasions/event_update_form.html'
    context_object_name = 'event'

    def form_valid(self, form):
        # set the last modified by field
        form.instance.last_modified_by = self.request.user

        return super(EventUpdateView, self).form_valid(form)

    def test_func(self):
        """
        Checks whether the user is an active user.
        :return: True if user is active, false otherwise.
        """
        return self.request.user.is_active


class EventListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    """
    A view that lists available events.

    This view is only available to users that are logged in and are marked as active in the system.
    """
    model = Event
    template_name = 'occasions/event_list.html'
    context_object_name = 'event_list'

    def test_func(self):
        """
        Checks whether the user is an active user.
        :return: True if user is active, false otherwise.
        """
        return self.request.user.is_active


class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    A view that handles event deletion.

    This view is only available to users that are logged in and are marked as active in the system.
    """
    model = Event
    success_url = reverse_lazy('occasions_event_list')
    context_object_name = 'event'
    template_name = 'occasions/event_confirm_delete.html'

    def test_func(self):
        """
        Checks whether the user is an active user.
        :return: True if user is active, false otherwise.
        """
        return self.request.user.is_active
