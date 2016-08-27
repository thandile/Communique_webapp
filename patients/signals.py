from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Patient, Enrollment

from user.models import UserActivity


@receiver(post_save, sender=Patient)
def post_patient_save_callback(sender, **kwargs):
    """
    Makes a record of the creation and updating of a patient by a user.
    """
    patient = kwargs['instance']
    if kwargs['created']:
        # new patient added
        if patient.created_by:
            description_str = "{0} registered a new patient named '{1}'.".format(patient.created_by.get_full_name(),
                                                                                 patient.__str__())
            UserActivity.objects.create(action=UserActivity.CREATE, actor=patient.created_by, object_name="Patient",
                                        object_url=patient.get_absolute_url(),
                                        object_identifier=patient.__str__(), description=description_str)
    else:
        # patient has been updated
        if patient.last_modified_by:
            description_str = "{0} updated a patient named '{1}'.".format(patient.last_modified_by.get_full_name(),
                                                                          patient.__str__())
            UserActivity.objects.create(action=UserActivity.UPDATE, actor=patient.last_modified_by,
                                        object_name="Patient", object_url=patient.get_absolute_url(),
                                        object_identifier=patient.__str__(), description=description_str)


@receiver(post_save, sender=Enrollment)
def post_enrollment_save_callback(sender, **kwargs):
    """
    Makes a record of the creation and modification of an enrollment
    """
    enrollment = kwargs['instance']
    if kwargs['created']:
        # enrollment created
        if enrollment.enrolled_by:
            description_str = "{0} enrolled patient '{1} in the program '{2}'.".format(
                enrollment.enrolled_by.get_full_name(), enrollment.patient.__str__(), enrollment.program.name)
            UserActivity.objects.create(action=UserActivity.CREATE, actor=enrollment.enrolled_by,
                                        object_name='Enrollment', object_url=enrollment.get_absolute_url(),
                                        description=description_str)