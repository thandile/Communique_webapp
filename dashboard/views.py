from django.shortcuts import render
from django.views.generic import View

# Create your views here.

class DashboardView(View):
    """CBV that displays the entire dashboard"""
    template_name = "dashboard/dashboard_view.html"

    def get(self, request):
        return render(request, self.template_name)