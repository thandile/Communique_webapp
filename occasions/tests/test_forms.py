from django.test import TestCase

import datetime

from occasions.forms import EventForm


class EventFormTestCase(TestCase):
    """
    Test cases for the event form.
    """

    def test_time_validation(self):
        """
        Tests that the submissions where start time is greater or equal to end time are invalidated
        """
        event_date = datetime.date.today()
        start_time = datetime.time(1)
        end_time = datetime.time(2)

        form = EventForm()
        self.assertFalse(form.is_bound)
        self.assertFalse(form.is_valid())

        data = {'name':'A dummy event','event_date':event_date, 'start_time':start_time, 'end_time':end_time }
        self.assertTrue(data['start_time'] < data['end_time'])

        form = EventForm(data)
        self.assertTrue(form.is_bound)
        self.assertTrue(form.is_valid())

        # reverse the start time and end time
        data['start_time'] = end_time
        data['end_time'] = start_time

        self.assertTrue(data['start_time'] > data['end_time'])
        form = EventForm(data)
        self.assertTrue(form.is_bound)
        self.assertFalse(form.is_valid())

    def test_date_validation(self):
        """
        Tests that the provided event data is not set in the past
        """
        event_date = datetime.date.today()
        start_time = datetime.time(1)
        end_time = datetime.time(2)

        form = EventForm()
        self.assertFalse(form.is_bound)
        self.assertFalse(form.is_valid())

        data = {'name':'A dummy event','event_date':event_date, 'start_time':start_time, 'end_time':end_time }
        current_date = datetime.date.today()

        self.assertFalse(data['event_date'] < current_date)

        form = EventForm(data)
        self.assertTrue(form.is_bound)
        self.assertTrue(form.is_valid())

        one_day = datetime.timedelta(days=1)

        tomorrow = current_date + one_day

        data['event_date'] = tomorrow
        self.assertFalse(data['event_date'] < current_date)
        form = EventForm(data)
        self.assertTrue(form.is_bound)
        self.assertTrue(form.is_valid())

        yesterday = current_date - one_day

        data['event_date'] = yesterday

        self.assertTrue(data['event_date'] < current_date)
        form = EventForm(data)
        self.assertTrue(form.is_bound)
        self.assertFalse(form.is_valid())
