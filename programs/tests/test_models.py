from django.test import TestCase
from django.core.urlresolvers import reverse

from programs.models import *


class ProgramTestCase(TestCase):
    """
    Test cases for the Program model.
    """

    def test_program_str(self):
        """
        A test case for the __str__ method of Program model.
        """
        program = Program.objects.create(name="sample Program", description="sample description")
        self.assertEqual(program.__str__(), 'Sample Program')

    def test_get_absolute_url(self):
        """
        A test case for the get_absolute_url method of the Program model.
        """
        program = Program.objects.create(name="sample Program", description="sample description")
        self.assertEqual(program.get_absolute_url(), reverse('programs_program_detail', kwargs={'pk':program.pk}))
