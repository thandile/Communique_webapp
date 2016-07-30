from django.test import TestCase
from services.models import PilotProgram, Patient

class PilotProgramTestCase(TestCase):
    def test_pilot_program_str(self):
        """ Test the __str__ method of the PilotProgram model."""
        pilot_program = PilotProgram.objects.create(name='sample pilot Program',
            description='sample description')
        self.assertEqual(pilot_program.__str__(), 'Sample Pilot Program')

class PatientTestCase(TestCase):
    def test_patient_str(self):
        """ Test teh __str__ method of the Patient model. """
        patient = Patient.objects.create(first_name='Michael',
            last_name='Kyeyune')
        self.assertEqual(patient.__str__(), 'Michael Kyeyune')
