from django import forms
from .models import Flat


class RieltorForm(forms.ModelForm):
    class Meta:
        model = Flat
        fields = ('area', 'price', 'description','link')

