from django.test import TestCase
from django.core.urlresolvers import reverse

from medical.models import MedicalReportType, MedicalReport
from patients.models import Patient


class MedicalReportTypeTestCase(TestCase):
    """
    Test cases for the medical report type model.
    """
    def setUp(self):
        MedicalReportType.objects.create(name='dummy type')

    def test_str(self):
        """
        Tests the __str__ method of the model
        """
        report_type = MedicalReportType.objects.get(id=1)
        self.assertEqual(report_type.__str__(), 'Dummy type')


class MedicalReportTestCase(TestCase):
    """
    Test cases for the medical report model.
    """
    def setUp(self):
        report_type = MedicalReportType.objects.create(name='dummy type')
        patient = Patient.objects.create(first_name='Jon', last_name='Snow')
        MedicalReport.objects.create(title='dummy report', report_type=report_type, patient=patient,
                                     notes='Sample notes')

    def test_str(self):
        """
        Tests the __str__ method of the model
        """
        medical_report = MedicalReport.objects.get(id=1)
        self.assertEqual(medical_report.__str__(), 'Dummy type report: Dummy report')