from django.test import TestCase
from django.contrib.auth.models import User

import datetime

from appointments.models import Appointment


class AppointmentTestCase(TestCase):
    """
    Test cases for the Appointment model.
    """

    def setUp(self):
        owner = User.objects.create_superuser('jon_snow', 'jonsnow@gmail.com', 'p@55words')
        appointment_date = datetime.date.today()
        start_time = datetime.time(1)
        end_time = datetime.time(start_time.hour + 1)
        Appointment.objects.create(title='a dummy appointment', owner=owner, appointment_date=appointment_date,
                                   start_time=start_time, end_time=end_time)

    def test_str(self):
        """
        A test case for the __str__ method of the model.
        """
        appointment = Appointment.objects.get(id=1)
        self.assertEqual(appointment.__str__(), 'A dummy appointment')
