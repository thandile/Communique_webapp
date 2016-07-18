from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from .models import Service
from .forms import ServiceForm

class ServiceListView(ListView):
    """
    A list view for the support service model.
    """
    model = Service
    template_name = 'support_services/service_list.html'
    context_object_name = 'service_list'

class ServiceDetailView(DetailView):
    """
    A detail view for the support service model.
    """
    model = Service
    template_name = 'support_services/service_view.html'
    context_object_name = 'service'

class ServiceCreateView(CreateView):
    """
    A create view for the support service model.
    """
    form_class = ServiceForm
    model = Service
    template_name = 'support_services/service_form.html'
