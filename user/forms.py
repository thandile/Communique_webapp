from django.forms import ModelForm

from .models import CommuniqueUser

class CommuniqueUserForm(ModelForm):
    """
    A form for the user model.
    """
    class Meta:
        model = CommuniqueUser
        fields = ('first_name', 'last_name', 'username', 'email', 'password')
