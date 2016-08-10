from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from .models import CommuniqueUser, Profile

class CommuniqueUserCreationForm(UserCreationForm):
    """
    A form used to register a new Communiqué user.
    """
    class Meta (UserCreationForm.Meta):
        model = CommuniqueUser
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name',
            'is_superuser', 'email',)

class CommuniqueUserUpdateForm(ModelForm):
    """
    A form used to update a user's active and superuser status.
    """
    class Meta:
        model = CommuniqueUser
        fields = ['is_active', 'is_superuser']

class Profile(ModelForm):
    """
    A form used to update a user profile's information
    """
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email']
