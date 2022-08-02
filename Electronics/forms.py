from django import forms
from .models import *

class addModels(forms.ModelForm):
    class Meta:
        model = electronicsProjects
        fields = ('name', 'catagory', 'video', 'image', 'description')