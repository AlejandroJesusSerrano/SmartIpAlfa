from django.forms import ModelForm
from .models import DevType

class DevTypeForm(ModelForm):
    class Meta:
        model = DevType
        fields = '__all__'
        