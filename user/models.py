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
    action = models.CharField(max_length=2, choices=ACTION_CHOICES)
    actor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_activities',
                              related_query_name='user_activity')
    date_time = models.DateTimeField(auto_now_add=True)
    object = models.TextField()
    object_url = models.TextField(blank=True, null=True)

