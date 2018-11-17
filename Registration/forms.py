from django import forms
from .models import EmailRegis

class RegisForm(forms.ModelForm):

    class Meta():
        model = Regis
        fields = [
            'FirstNameField',
            'lastNameField',
            'emailField',
        ]