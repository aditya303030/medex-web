from django import forms 
from .models import DonationForm

class FormDonationForm(forms.ModelForm):
    class Meta:
        model = DonationForm
        fields = "__all__"