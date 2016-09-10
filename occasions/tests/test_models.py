from django.test import TestCase

import datetime

from occasions.models import Event


class EventTestCase(TestCase):
    """
    Test cases for the Event model.
    """
    def setUp(self):
        event_date = datetime.date.today()
        start_time = datetime.time(1)
        end_time = datetime.time(2)
        Event.objects.create(name='a dummy event', event_date=event_date, start_time=start_time, end_time=end_time)

    def test_str(self):
        """
        Tests the __str__ method of the model
        """
        event = Event.objects.get(id=1)
        self.assertEqual(event.__str__(), 'A dummy event')