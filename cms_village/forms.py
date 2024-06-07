from django import forms
from cms_village.models import *


class AccommodationForm(forms.ModelForm):
    class Meta:
        model = Accommodation
        fields = '__all__'
