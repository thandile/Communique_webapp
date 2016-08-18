from django.test import TestCase

from patients.models import Patient


class PatientTestCase(TestCase):
    """
    Test cases for the Patient model.
    """

    def test_patient_str(self):
        """
        A test case for the __str__ method for the Patient model.
        """
        patient = Patient.objects.create(first_name='Jon', last_name='Snow')
        self.assertEqual(patient.__str__(), 'Jon Snow')

        patient.middle_name = 'Bastard'
        patient.save()
        self.assertEqual(patient.__str__(), 'Jon Bastard Snow')