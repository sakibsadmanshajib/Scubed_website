from django import forms
from django.utils import timezone

class AddScreen(forms.Form):

    diagonal_size = forms.DecimalField()
    category = forms.CharField(max_length=200)
    resolution = forms.CharField(max_length=200)