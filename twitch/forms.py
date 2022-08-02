from django import forms
from .models import *

class addModels(forms.ModelForm):
    class Meta:
        model = twitchStreaming
        fields = ('name', 'catagory', 'video', 'description')