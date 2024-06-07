from django import forms
from cms_calendar.models import *


class MarketForm(forms.ModelForm):
    class Meta:
        model = Market
        fields = '__all__'


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'

