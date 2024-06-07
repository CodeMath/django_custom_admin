from django import forms
from cms_bbs.models import *


class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = '__all__'


class GallerySessionForm(forms.ModelForm):
    class Meta:
        model = GallerySession
        fields = '__all__'
