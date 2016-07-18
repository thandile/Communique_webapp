from django.forms import ModelForm
from .models import Service

class ServiceForm(ModelForm):
    """
    A ModelForm for the Service class.
    """
    class Meta:
        model = Service
        fields = '__all__'

    def is_valid(self):
        # fill in the slug component of the Service model
        self.instance.slug = self.instance.generate_slug(self.instance.name)
        return super(ModelForm, self).is_valid()
