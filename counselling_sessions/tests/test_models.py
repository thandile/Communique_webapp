from django.test import TestCase

from django.core.urlresolvers import reverse

from counselling_sessions.models import *


class CounsellingSessionTypeTestCase(TestCase):
    """
    Test cases for the CounsellingSessionType model.
    """
    def test_counselling_session_type_str(self):
        """
        A test case for the __str__ method of the model.
        """
        session_type = CounsellingSessionType.objects.create(name='dummy type')
        self.assertEqual(session_type.__str__(), 'Dummy Type')

    def test_get_absolute_url(self):
        """
        A test case for the get_absolute_url method for the model.
        """
        session_type = CounsellingSessionType.objects.create(name='dummy type')
        self.assertEqual(session_type.get_absolute_url(), reverse('counselling_sessions_type_detail',
                                                                              kwargs={'pk':session_type.pk}))

    def test_get_update_url(self):
        """
        A test case for the get_update_url method for the model.
        """
        session_type = CounsellingSessionType.objects.create(name='dummy type')
        self.assertEqual(session_type.get_update_url(), reverse('counselling_sessions_type_update',
                                                                            kwargs={'pk':session_type.pk}))

    def test_get_delete_url(self):
        """
        A test case for the get_delete_url method for the model.
        """
        session_type = CounsellingSessionType.objects.create(name='dummy Type')
        self.assertEqual(session_type.get_delete_url(), reverse('counselling_sessions_type_delete',
                                                                kwargs={'pk':session_type.pk}))


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