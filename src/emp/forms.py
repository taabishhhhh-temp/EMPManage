from django import forms
from django.core.exceptions import ValidationError
from django.db.models import fields
from .models import Employ

# class EmpForm(forms.Form):
    

class EmployForm(forms.ModelForm):   #Model Form
    class Meta:
        model = Employ
        fields = [
            'empid',
            'employID',
            'fname',
            'lname',
            'personalEmail',
            'fladdraEmail',
            'mobile',
            'position',
            'github',
            'education',
            'address',
            # 'joinedOn'
        ]

# class 