from django.test import TestCase

from counselling_sessions.models import *


class CounsellingSessionTypeTestCase(TestCase):
    """
    Test cases for the CounsellingSessionType model.
    """
    def test_counselling_session_type_str(self):
        """
        A test case for the __str__ method of the model.
        """
        counselling_session_type = CounsellingSessionType.objects.create(name='dummy type')
        self.assertEqual(counselling_session_type.__str__(), 'Dummy Type')


class CounsellingSessionTestCase(TestCase):
    """
    Test cases for the CounsellingSession model.
    """
    def test_counselling_session_str(self):
        """
        A test case for the __str__ method of the model.
        """
        session_type = CounsellingSessionType.objects.create(name='dummy type')
        patient = Patient.objects.create(first_name='Jon', last_name='Snow')
        counselling_session = CounsellingSession.objects.create(patient=patient, counselling_session_type=session_type)
        self.assertEqual(counselling_session.__str__(), 'A Dummy Type session for Jon Snow')