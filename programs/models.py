from django.db import models
from django.core.urlresolvers import reverse


class Program(models.Model):
    """
    A class representing a program/initiative to provide a service to patients.
    """
    name = models.CharField(verbose_name="Program name", unique=True, max_length=100)
    description = models.TextField(verbose_name="Description")
    date_created = models.DateField(auto_now_add=True)
    date_last_modified = models.DateField(auto_now=True)
    is_open = models.BooleanField(verbose_name="Is open", default=True, help_text='Is this program ongoing or closed?')

    def __str__(self):
        return self.name.title()

    def get_absolute_url(self):
        return reverse('programs_program_detail', kwargs={'pk':self.pk})

    def get_update_url(self):
        return reverse('programs_program_update', kwargs={'pk':self.pk})