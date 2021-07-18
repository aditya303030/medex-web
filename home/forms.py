from .models import *
from django import forms
from django.forms import ModelForm,fields

class Medicinehompage(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = "__all__"