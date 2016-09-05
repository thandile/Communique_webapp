from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import CounsellingSessionType, CounsellingSession

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
            description_str = "{0} added a new session type named '{1}'.".format(session_type.created_by.get_full_name(),
                                                                                 session_type)
            action = UserActivity.CREATE
        else:
            description_str = "{0} modified the session type name '{1}'.".format(
                session_type.last_modified_by.get_full_name(), session_type)
            action = UserActivity.UPDATE

        UserActivity.objects.create(action=action, actor=actor, object_name='Session Type',
                                    object_url=session_type.get_absolute_url(), object_identifier=session_type.__str__(),
                                    description=description_str)


@receiver(post_save, sender=CounsellingSession)
def post_session_save_callback(sender, **kwargs):
    """
    Makes a record of the creation and updating of a CounsellingSession by a user.
    """
    counselling_session = kwargs['instance']

    if counselling_session.created_by or counselling_session.last_modified_by:
        description_str = None
        action = None
        actor = counselling_session.last_modified_by

        if kwargs['created']:
            description_str = "{0} added a new session: {1}.".format(counselling_session.last_modified_by.get_full_name(),
                                                                     counselling_session)
            action = UserActivity.CREATE
        else:
            description_str = "{0} updated the session: {1}.".format(counselling_session.last_modified_by.get_full_name(),
                                                                     counselling_session)
            action = UserActivity.UPDATE

        UserActivity.objects.create(action=action, actor=actor, object_name='Session',
                                    object_url=counselling_session.get_absolute_url(),
                                    object_identifier=counselling_session.__str__(), description=description_str)