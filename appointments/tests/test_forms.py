from django.test import  TestCase
from django.contrib.auth.models import User

from appointments.forms import AppointmentForm

from patients.models import Patient

import datetime


class AppointmentFormTestCase(TestCase):
    """
    Test cases for the appointment form.
    """

    def test_clean(self):
        """
        Tests that the clean method invalidates submissions where start time is greater or equal to end time.
        """
        User.objects.create_superuser('jon_snow', 'jonsnow@gmail.com', 'p@55words')
        Patient.objects.create(first_name='Jon', last_name='Snow')

        appointment_date = datetime.date.today()
        start_time = datetime.time(1)
        end_time = datetime.time(start_time.hour + 1)
        title = 'A dummy title'

        form = AppointmentForm()
        self.assertFalse(form.is_bound)
        self.assertFalse(form.is_valid())

        # data when start time < endtime
        data = {'title':title, 'appointment_date':appointment_date, 'start_time':start_time, 'patient':1,
                'owner':1, 'end_time':end_time}
        self.assertTrue(data['start_time'] < data['end_time'])

        form = AppointmentForm(data)
        self.assertTrue(form.is_bound)
        self.assertTrue(form.is_valid())

        # reverse the start time and end time
        data['start_time'] = end_time
        data['end_time'] = start_time

        self.assertTrue(data['start_time'] > data['end_time'])

        form = AppointmentForm(data)
        self.assertTrue(form.is_bound)
        self.assertFalse(form.is_valid())

