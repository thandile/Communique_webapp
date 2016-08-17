from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Program

from user.models import UserActivity


@receiver(post_save, sender=Program)
def post_program_save_callback(sender, **kwargs):
    """
    Makes a record of the creation and updating of a Program by a user.
    """
    program = kwargs['instance']
    if kwargs['created']:
        # new program has been opened, note user activity for it
        if program.created_by:
            description_str = "{0} opened a new program titled '{1}'.".format(program.created_by.get_full_name(),
                                                                              program.name)
            UserActivity.objects.create(action=UserActivity.OPEN, actor=program.created_by, object_name="Program",
                                        object_url=program.get_absolute_url(), description=description_str)
    else:
        # program has been updated, yet to discern what type of update i.e closed
        if program.last_modified_by:
            description_str = "{0} update a program titled '{1}'.".format(program.last_modified_by.get_full_name(),
                                                                          program.name)
            UserActivity.objects.create(action=UserActivity.UPDATE, actor=program.last_modified_by,
                                        object_name="Program", object_url=program.get_absolute_url(),
                                        description=description_str)

