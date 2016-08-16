from django.forms import ModelForm
from .models import Program


class ProgramForm(ModelForm):
    """
    A model form for the Program model.
    """
    class Meta:
        model = Program
        fields = ('name', 'description', 'is_open')