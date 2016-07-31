from django.forms import ModelForm
from django.contrib.auth.models import User

class UserForm(ModelForm):
    """
    A form for the user model.
    """
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')
