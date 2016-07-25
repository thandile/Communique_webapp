from django.forms import ModelForm
from .models import PilotProgram, Patient

class PilotProgramForm(ModelForm):
    """
    A model form for the pilot program model.
    """
    class Meta:
        model = PilotProgram
        fields =  ('name', 'description')

class PatientForm(ModelForm):
    """
    A model form the patient model.
    """
    class Meta:
        model = Patient
        fields = ('first_name', 'last_name', 'birth_date')
