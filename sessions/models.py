from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from patients.models import Patient


class SessionType(models.Model):
    """
    A model representing the possible type of a session.
    """
    name = models.CharField(verbose_name='Session type', unique=True, max_length=100,
                            help_text='The name to be given to this session type.')
    description = models.TextField(verbose_name='Description', blank=True, null=True,
                                   help_text='The description of this session type. This field is optional.')
    date_created = models.DateField(verbose_name='Date created', auto_now_add=True,
                                    help_text='The date on which the session type was created.')
    created_by = models.ForeignKey(User, verbose_name='Created by', on_delete=models.SET_NULL, blank=True, null=True,
                                   related_name='created_session_types', related_query_name='created_session_type')
    date_last_modified = models.DateField(verbose_name='Date last modified', auto_now=True,
                                          help_text='The date on which the session type was last modified')
    last_modified_by = models.ForeignKey(User, verbose_name='Modified by', on_delete=models.SET_NULL, blank=True,
                                         null=True, related_name='modified_session_types',
                                         related_query_name='modified_session_type')

    def __str__(self):
        return self.name.title()


class Session(models.Model):
    """
    A model representing a session i.e an interaction between a patient and facilitator.
    """
    session_type = models.ForeignKey(SessionType, verbose_name='Session type', on_delete=models.SET_NULL,
                                     related_name='sessions', related_query_name='session',
                                     help_text='The category which this session falls into')
    patient = models.ForeignKey(Patient, verbose_name='Patient', on_delete=models.CASCADE, related_name='sessions',
                                related_query_name='session', help_text='The patient for whom the session is for')
    notes = models.TextField(verbose_name='Notes', blank=True, null=True,
                             help_text='Any additional notes on the session')
    created_by = models.ForeignKey(User, verbose_name='Administered by', on_delete=models.SET_NULL, blank=True,
                                   null=True, related_name='created_sessions', related_query_name='created_session',
                                   help_text='The user that administered the session')
    date_created = models.DateTimeField(verbose_name='Date created', auto_now_add=True,
                                        help_text='The date on which the session was created')
    last_modified_by = models.ForeignKey(User, verbose_name='Last modified by', on_delete=models.SET_NULL, blank=True,
                                         null=True, related_name='modified_sessions',
                                         related_query_name='modified_session',
                                         help_text='The user to last modify the session')
    date_last_modified = models.DateTimeField(verbose_name='Date last modified', auto_now=True,
                                              help_text='The date on which the session was last modified')
    
    def __str__(self):
        return "A {0} session for {1}".format(self.session_type, self.patient)


