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


class TreasuryOperationForm(forms.ModelForm):
    class Meta:
        fields = [ 'operation_value', 'operation_description' ]
        model = TreasuryOperation
        widgets = {
            'operation_value' : forms.NumberInput(attrs={'class':'form-control', 'min':0, 'name':'op_value'}),        
            'operation_description' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'تفاصيل العملية......', 'name':'description'}),        
        }   
        

class TreasuryOperationDeleteForm(forms.ModelForm):
    class Meta:
        fields = ['deleted_operation']
        model = TreasuryOperation
        widgets = {
            'deleted_operation' : forms.HiddenInput()
        }        

