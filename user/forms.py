from django.contrib.auth.forms import UserCreationForm

from .models import CommuniqueUser

class CommuniqueUserCreationForm(UserCreationForm):
    """
    A form used to register a new Communiqué user.
    """
    class Meta (UserCreationForm.Meta):
        model = CommuniqueUser
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name',
            'is_superuser', 'email',)
