from django.forms import ModelForm
from .models import PilotProgram

class PilotProgramForm(ModelForm):
    """
    A model form for the pilot program
    """
    class Meta:
        model = PilotProgram
        fields =  ('name', 'description')
