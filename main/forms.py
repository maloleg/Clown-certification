from .models import Data
from django.forms import ModelForm

class DataForm(ModelForm):
    class Meta:
        model = Data
