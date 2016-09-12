from django.test import TestCase
from django.core.urlresolvers import reverse

from programs.models import Program


class ProgramTestCase(TestCase):
    """
    Test cases for the Program model.
    """
    def setUp(self):
        Program.objects.create(name='sample Program', description='sample description')

    def test_program_str(self):
        """
        A test case for the __str__ method of Program model.
        """
        program = Program.objects.get(id=1)
        self.assertEqual(program.__str__(), 'Sample Program')

    def test_get_absolute_url(self):
        """
        A test case for the get_absolute_url method of the Program model.
        """
        program = Program.objects.get(id=1)
        self.assertEqual(program.get_absolute_url(), reverse('programs_program_detail', kwargs={'pk':program.pk}))

    def test_get_update_url(self):
        """
        A test case for the get_update_url method of the Program model.
        """
        program = Program.objects.get(id=1)
        self.assertEqual(program.get_update_url(), reverse('programs_program_update', kwargs={'pk':program.pk}))

    def test_get_delete_url(self):
        """
        A test case for the get_delete_url method of the Program model.
        """
        program = Program.objects.get(id=1)
        self.assertEqual(program.get_delete_url(), reverse('programs_program_delete', kwargs={'pk':program.pk}))
