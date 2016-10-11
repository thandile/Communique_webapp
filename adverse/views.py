from django.core.urlresolvers import reverse_lazy

from .models import EmergencyContact, AdverseEvent, AdverseEventType
from communique.views import (CommuniqueCreateView, CommuniqueDetailView, CommuniqueListView, CommuniqueUpdateView,
                              CommuniqueDeleteView)
from .forms import AdverseEventForm


class EmergencyContactListView(CommuniqueListView):
    """
    A view to list all the emergency contacts in the system
    """
    model = EmergencyContact
    template_name = 'adverse/emergency_contact_list.html'
    context_object_name = 'emergency_contact_list'


class EmergencyContactCreateView(CommuniqueCreateView):
    """
    A view to handle the form for creation of an emergency contact
    """
    model = EmergencyContact
    fields = ['name', 'email']
    template_name = 'adverse/emergency_contact_form.html'


class EmergencyContactDetailView(CommuniqueDetailView):
    """
    A view to display details of an emergency contact
    """
    model = EmergencyContact
    template_name = 'adverse/emergency_contact_view.html'
    context_object_name = 'emergency_contact'


class EmergencyContactUpdateView(CommuniqueUpdateView):
    """
    A view to handle the update form for a drug
    """
    model = EmergencyContact
    fields = ['name', 'email']
    template_name = 'adverse/emergency_contact_update_form.html'
    context_object_name = 'emergency_contact'


class EmergencyContactDeleteView(CommuniqueDeleteView):
    """
    A view to handle the deletion of an emergency contact
    """
    model = EmergencyContact
    success_url = reverse_lazy('adverse_emergency_contact_list')
    context_object_name = 'emergency_contact'
    template_name = 'adverse/emergency_contact_confirm_delete.html'


class AdverseEventTypeListView(CommuniqueListView):
    """
    A view to list all the adverse event types
    """
    model = AdverseEventType
    template_name = 'adverse/adverse_event_type_list.html'
    context_object_name = 'adverse_event_type_list'


class AdverseEventTypeCreateView(CommuniqueCreateView):
    """
    A view to handle the form for creation of an adverse event type
    """
    model = AdverseEventType
    fields = ['name', 'description', 'emergency_contacts']
    template_name = 'adverse/adverse_event_type_form.html'


class AdverseEventTypeDetailView(CommuniqueDetailView):
    """
    A view to display the details of an adverse event type
    """
    model = AdverseEventType
    template_name = 'adverse/adverse_event_type_view.html'
    context_object_name = 'adverse_event_type'


class AdverseEventTypeUpdateView(CommuniqueUpdateView):
    """
    A view to handle the update form of an adverse event type
    """
    model = AdverseEventType
    fields = ['name', 'description', 'emergency_contacts']
    template_name = 'adverse/adverse_event_type_update_form.html'
    context_object_name = 'adverse_event_type'


class AdverseEventTypeDeleteView(CommuniqueDeleteView):
    """
    A view to handle deletion of an adverse event type
    """
    model = AdverseEventType
    success_url = reverse_lazy('adverse_event_type_list')
    context_object_name = 'adverse_event_type'
    template_name = 'adverse/adverse_event_type_confirm_delete.html'


class AdverseEventListView(CommuniqueListView):
    """
    A view to list all the adverse events
    """
    model = AdverseEvent
    template_name = 'adverse/adverse_event_list.html'
    context_object_name = 'adverse_event_list'


class AdverseEventCreateView(CommuniqueCreateView):
    """
    A view to handle the form for creation of an adverse event
    """
    model = AdverseEvent
    form_class = AdverseEventForm
    template_name = 'adverse/adverse_event_form.html'


class AdverseEventDetailView(CommuniqueDetailView):
    """
    A view to display the details of an adverse event
    """
    model = AdverseEvent
    template_name = 'adverse/adverse_event_view.html'
    context_object_name = 'adverse_event'


class AdverseEventUpdateView(CommuniqueUpdateView):
    """
    A view to handle the update form of an adverse event
    """
    model = AdverseEvent
    fields = ['event_date', 'notes']
    template_name = 'adverse/adverse_event_update_form.html'
    context_object_name = 'adverse_event'


class AdverseEventDeleteView(CommuniqueDeleteView):
    """
    A view to handle deletion of an adverse event type
    """
    model = AdverseEvent
    success_url = reverse_lazy('adverse_event_list')
    context_object_name = 'adverse_event'
    template_name = 'adverse/adverse_event_confirm_delete.html'