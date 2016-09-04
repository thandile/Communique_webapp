from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import CounsellingSessionType

from user.models import UserActivity


@receiver(post_save, sender=CounsellingSessionType)
def post_session_type_save_callback(sender, **kwargs):
    """
    Makes a record of the creation and updating of a CounsellingSessionType by a user.
    """
    session_type = kwargs['instance']

    if session_type.created_by or session_type.last_modified_by:
        description_str = None
        action = None
        actor = session_type.last_modified_by

        if kwargs['created']:
            description_str = "{0} added a new session type named '{1}'.".format(session_type.created_by, session_type)
            action = UserActivity.CREATE
        else:
            description_str = "{0} modified the session type name '{1}'.".format(session_type.last_modified_by,
                                                                                 session_type)
            action = UserActivity.UPDATE

        UserActivity.objects.create(action=action, actor=actor, object_name='Session Type',
                                    object_url=session_type.get_absolute_url(), object_identifier=session_type.__str__(),
                                    description=description_str)