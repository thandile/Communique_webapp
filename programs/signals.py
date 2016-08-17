from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Program


@receiver(post_save, sender=Program)
def post_program_save_callback(sender, **kwargs):
    """
    Records the user that has created or updated a program.
    """
    if kwargs['created']:
        # new program has been created
        print('A new object is created')