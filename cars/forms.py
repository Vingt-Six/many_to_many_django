from django import forms
from .models import *

class ColorForm(forms.ModelForm):
    class Meta:
        model = Color
        fields = '__all__'

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'