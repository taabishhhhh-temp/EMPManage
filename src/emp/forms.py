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
            'joinedOn'
        ]

    
    def clean_employID(self):
        value = self.cleaned_data.get('employID')
        x = str(value)
        if len(x) == 4:
            return value
            # if str(value).startswith('10'):
        raise forms.ValidationError('Employ ID must be 4 digit and should start with 10')

    def clean_fname(self):  #Validator
        value = self.cleaned_data.get('fname')
        return value.title()

    def clean_lname(self):
        value = self.cleaned_data.get('lname')
        return value.title()

    def clean_fladdraEmail(self):
        email = self.cleaned_data.get('fladdraEmail')
        mail = str(email)
        if mail.endswith('@fladdra.com'):
            return email
        raise forms.ValidationError("Fladdra Email must end with '@fladdra.com'")

    def clean_mobile(self):
        value = self.cleaned_data.get('mobile')
        if len(str(value)) != 10:
            raise forms.ValidationError('Mobile number must be 10 digit!')
        else:
            return value

    # def clean_EMPID(self):
    #     value = self.cleaned_data.get('empid')
    #     if int(value) < 100 or int(value) > 999:
    #         raise forms.ValidationError('Empid must be a 3 digit number!')
    #     else:
    #         return value
    
    def clean_position(self):
        value = str(self.cleaned_data.get('position'))
        pos_list = ['Intern', 'Senior Developer', 'Junior Developer', 'HR', '-', 'test']
        if value in pos_list:
            return value.title()
        else:
            raise forms.ValidationError('This position is not valid!')

    # def clean_github(self):
    #     value = self.cleaned_data.get('Github')

    #     if str(value).startswith('github.com/'):
    #         return value
    #     raise forms.ValidationError('Github Username should start with github.com/')
            
