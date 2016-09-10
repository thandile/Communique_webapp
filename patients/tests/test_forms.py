from django.test import TestCase
from django.contrib.auth.models import User

import datetime

from patients.forms import PatientAppointmentForm


class PatientAppointmentFormTestCase(TestCase):
    """
    Test cases for the patient appointment form.
    """
    def setUp(self):
        User.objects.create_superuser('jon_snow', 'jonsnow@gmail.com', 'p@55words')

    def test_time_validation(self):
        """
        Tests that the clean method invalidates submissions where start time is greater or equal to end time.
        """
        appointment_date = datetime.date.today()
        start_time = datetime.time(1)
        end_time = datetime.time(2)
        title = 'A dummy title'

        form = PatientAppointmentForm()
        self.assertFalse(form.is_bound)
        self.assertFalse(form.is_valid())

        data = {'title':title, 'appointment_date':appointment_date, 'start_time':start_time, 'end_time':end_time,
                'owner':1}

        self.assertTrue(data['start_time'] < data['end_time'])

        form = PatientAppointmentForm(data)
        self.assertTrue(form.is_bound)
        self.assertTrue(form.is_valid())

        # reverse the start time and end time
        data['start_time'] = end_time
        data['end_time'] = start_time

        self.assertTrue(data['start_time'] > data['end_time'])

        form = PatientAppointmentForm(data)
        self.assertTrue(form.is_bound)
        self.assertFalse(form.is_valid())

    def test_date_validation(self):
        """
        Tests that the provided appointment date is not set in the past
        """
        appointment_date = datetime.date.today()
        start_time = datetime.time(1)
        end_time = datetime.time(2)
        title = 'A dummy title'

        form = PatientAppointmentForm()
        self.assertFalse(form.is_bound)
        self.assertFalse(form.is_valid())

        data = {'title':title, 'appointment_date':appointment_date, 'start_time':start_time, 'end_time':end_time,
                'owner':1}
        current_date = datetime.date.today()

        self.assertFalse(data['appointment_date'] < current_date)

        form = PatientAppointmentForm(data)
        self.assertTrue(form.is_bound)
        self.assertTrue(form.is_valid())

        one_day = datetime.timedelta(days=1)

        tomorrow = current_date + one_day

        data['appointment_date'] = tomorrow

        self.assertFalse(data['appointment_date'] < current_date)
        form = PatientAppointmentForm(data)
        self.assertTrue(form.is_bound)
        self.assertTrue(form.is_valid())

        yesterday = current_date - one_day

        data['appointment_date'] = yesterday

        self.assertTrue(data['appointment_date'] < current_date)
        form = PatientAppointmentForm(data)
        self.assertTrue(form.is_bound)
        self.assertFalse(form.is_valid())