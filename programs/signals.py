from django.db.models.signals import post_save
from django.dispatch import receiver

from notifications.signals import notify

from .models import Program


@receiver(post_save, sender=Program)
def post_program_save_callback(sender, **kwargs):
    """
    Makes a record of the creation and updating of a Program by a user.
    """
    program = kwargs['instance']

    # check whether the user responsible for saving the object is available
    if program.last_modified_by:
        # check whether the object was created or updated

        if kwargs['created']:
            verb = 'added'
        else:
            verb = 'updated'

        summary = "{0} the program: {1}".format(verb, program)

        description = program.description

        notify.send(program.last_modified_by, recipient=program.last_modified_by, verb=summary, action_object=program,
                    level='success', description=description, target=program)
