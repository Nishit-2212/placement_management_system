from django import forms
from .models import *

class stuform(forms.ModelForm):
    class Meta:
        model=Student
        fields= '__all__'

