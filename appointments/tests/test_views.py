from django.core.urlresolvers import reverse

from communique.tests import ViewsTestCase


class AppointmentCreateViewTestCase(ViewsTestCase):
    """
    Test cases for the view to create an appointment.
    """
    view_name = 'appointments_appointment_create'
    view_template_name = 'appointments/appointment_form.html'
    view_url = reverse(view_name)

    def test_active_user_access(self):
        self.only_active_user_access_test(self.view_url, self.view_template_name)