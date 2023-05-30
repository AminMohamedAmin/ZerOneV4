from django import forms
from .models import *


class TreasuryForm(forms.ModelForm):
    class Meta:
        model = Treasury
        exclude = ['deleted']
        widgets = {
            'treasury_name' : forms.TextInput(attrs={'class':'form-control'}),
            'treasury_balance' : forms.NumberInput(attrs={'class':'form-control', 'min':0}),        
        }

class TreasuryDeleteForm(forms.ModelForm):
    class Meta:
        fields = ['deleted']
        model = Treasury
        widgets = {
            'deleted' : forms.HiddenInput()
        }        
        
        