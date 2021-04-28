from django import forms
from .models import Employee


class Trainlog(forms.ModelForm):

    class Meta:
        model = Train
        fields = __all__
        
