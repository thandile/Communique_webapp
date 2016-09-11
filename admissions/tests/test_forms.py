from django.test import TestCase

from admissions.forms import AdmissionForm
from patients.models import Patient

import datetime


class AdmissionFormTestCase(TestCase):
    """
    Test cases for the admission form.
    """
    def setUp(self):
        Patient.objects.create(first_name='Jon', last_name='Snow')

    def test_date_validation(self):
        """
        Tests that the form invalidates submissions where the admission date is greater than discharge date
        """
        form = AdmissionForm()
        self.assertFalse(form.is_bound)
        self.assertFalse(form.is_valid())

        current_date = datetime.date.today()
        one_day = datetime.timedelta(days=1)
        tomorrow = current_date + one_day

        data = {}
        data['patient'] = 1
        data['health_centre'] = "St.Michael's hospital"
        data['notes'] = 'dummy notes'
        data['admission_date'] = current_date
        data['discharge_date'] = tomorrow

        self.assertTrue(data['admission_date'] < data['discharge_date'])
        form = AdmissionForm(data)
        self.assertTrue(form.is_bound)
        self.assertTrue(form.is_valid())

        data['admission_date'] = tomorrow
        data['discharge_date'] = current_date

        self.assertFalse(data['admission_date'] < data['discharge_date'])
        form = AdmissionForm(data)
        self.assertTrue(form.is_bound)
        self.assertFalse(form.is_valid())

