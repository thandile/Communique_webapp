from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models


class CommuniqueUser(User):
    """
    A proxy model for the default User model, adding extra methods.
    """
    class Meta:
        proxy = True

    def get_absolute_url(self):
        return reverse('user_communique_user_detail', kwargs={'pk':self.pk})

    def get_update_url(self):
        return reverse('user_communique_user_update', kwargs={'pk':self.pk})


class Profile(User):
    """
    A proxy model for the default User model, masquerading as a Profile.
    """
    class Meta:
        proxy = True

    def get_absolute_url(self):
        return reverse('user_profile_detail', kwargs={'pk':self.pk})

    def get_update_url(self):
        return reverse('user_profile_update', kwargs={'pk':self.pk})


class UserActivity(models.Model):
    """
    A model to log user activity with regards to CRUD for other models.
    """
    CREATE = 'CR'
    UPDATE = 'UP'
    DELETE = 'DL'
    OPEN = 'OP'
    CLOSE = 'CL'
    ACTIVATE = 'AC'
    DEACTIVATE = 'DE'

    ACTION_CHOICES = (
        (CREATE, 'Created'),
        (UPDATE, 'Updated'),
        (DELETE, 'Deleted'),
        (OPEN, 'Opened'),
        (CLOSE, 'Closed'),
        (ACTIVATE, 'Activated'),
        (DEACTIVATE, 'Deactivated'),
    )
    action = models.CharField(max_length=2, choices=ACTION_CHOICES,
                              help_text='The category of the action taken by the user')
    actor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_activities',
                              related_query_name='user_activity',
                              help_text='The user whom the action is attributed to')
    date_time = models.DateTimeField(auto_now_add=True, help_text='The time and date the activity took place')
    object_name = models.CharField(max_length=100, default='Model',
                                   help_text='The model with which the user was interacting')
    object_url = models.CharField(max_length=100, blank=True, null=True,
                                  help_text='The url to the model that the user interacted with')
    object_identifier = models.CharField(max_length=100, blank=True, null=True,
                                         help_text='The unique identifier for the model the user interacted with')
    description = models.TextField(blank=True, null=True, help_text='A summary of the interaction that took place')

    class Meta:
        ordering = ['-date_time']

