from dataclasses import field

from django import forms
from .models import Customer



class AccountDetailsForm(forms.Form):
   
    firstName = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control",    
    }), required=False)
    userName = forms.CharField(widget=forms.TextInput(attrs={
    'class': 'form-control',
    }),required=False)
    lastName = forms.CharField(widget=forms.TextInput(attrs={
    'class': 'form-control',
   
    }),required=False)
    street = forms.CharField(widget=forms.TextInput(attrs={
    'class': 'form-control',
    
    }),required=False)
    city = forms.CharField(widget=forms.TextInput(attrs={
    'class': 'form-control',
    
    }), required=False)
    district = forms.CharField(widget=forms.TextInput(attrs={
    'class': 'form-control',
    
    }),required=False)
    email = forms.CharField(widget=forms.TextInput(attrs={
    'class': 'form-control',
    }),required=False)
    phoneNumber = forms.IntegerField(widget=forms.TextInput(attrs={
    'class': 'form-control',
    }),required=False)
  