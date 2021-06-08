from django import forms
from django.db.models import fields
from .models import Employ

class EmployForm(forms.ModelForm):
    class Meta:
        model = Employ
        fields = [
            'empid',
            'fname',
            'lname',
            'email',
            'mobile',
            'position'
        ]