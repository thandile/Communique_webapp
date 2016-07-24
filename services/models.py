from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class PilotProgram(models.Model):
    """
    A class representing a pilot program for the MSF.
    """
    name = models.CharField(verbose_name="Name", unique=True, max_length=100)
    description = models.TextField(verbose_name="Description")

    def __str__(self):
        return self.name.title()

    def get_absolute_url(self):
        # return reverse('services_pilot_program_detail', kwargs={'slug':self.slug})
        pass

    def get_update_url(self):
        pass

    def get_delete_url(self):
        pass

    class Meta:
        ordering = ['name']

class Patient(models.Model):
    """
    A class representing a Patient.
    A patient has a first name, last name and birth date.
    """
    first_name = models.CharField(verbose_name="First Name", max_length=60)
    last_name = models.CharField(verbose_name="Last Name", max_length=100)
    birth_date = models.DateField(verbose_name="Birth Date")

    def __str__(self):
        name = self.first_name + " " + self.last_name
        return name

    def get_absolute_url(self):
        pass

    def get_update_url(self):
        pass

    def get_delete_url(self):
        pass

    class Meta:
        ordering = ['last_name']
