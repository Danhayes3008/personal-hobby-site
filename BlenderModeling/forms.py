from django import forms
from .models import *

class addModels(forms.ModelForm):
    class Meta:
        model = blenderModels
        fields = ('name', 'catagory', 'video', 'image', 'description')