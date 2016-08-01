from django.contrib.auth.models import User

class CommuniqueUser(User):
    """
    A proxy model for the default User model, adding extra methods.
    """
    class Meta:
        proxy = True

    def get_absolute_url(self):
        pass

    def get_update_url(self):
        pass

    def get_deactivate_url(self):
        pass
