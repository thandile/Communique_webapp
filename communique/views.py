from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

"""
Views for the web app
"""
class DashboardTemplateView(LoginRequiredMixin, TemplateView):
    """
    A view to display the dashboard home template.
    """
    template_name = 'dashboard_view.html'
