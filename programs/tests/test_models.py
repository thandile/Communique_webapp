from django.test import TestCase
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