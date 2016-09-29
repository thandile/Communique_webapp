from django import forms

import datetime

from .models import Event


class EventForm(forms.ModelForm):
    """
    A form used to create and update an event
    """
    class Meta:
        model = Event
        fields = ['name', 'event_date', 'start_time', 'end_time', 'description']

    def clean(self):
        # check that the start time is less than the end time
        start_time = self.cleaned_data.get('start_time')
        end_time = self.cleaned_data.get('end_time')

        if start_time and end_time:
            if start_time >= end_time:
                raise forms.ValidationError('The start time cannot be greater than or equal to the end time',
                                            code='invalid')

        return super(EventForm, self).clean()

    def clean_event_date(self):
        # check that the provided event date is not in the past
        event_date = self.cleaned_data.get('event_date')

        if event_date:
            current_date = datetime.date.today()
            if event_date < current_date:
                raise forms.ValidationError('The event date cannot be set in the past', code='invalid')

        return event_date