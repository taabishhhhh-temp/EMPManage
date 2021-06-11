from django import forms
from django.db.models import fields
from .models import Employ

class EmployForm(forms.ModelForm):   #Model Form
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

    def clean_fname(self):  #Validator
        value = self.cleaned_data.get('fname')
        return value.title()

    def clean_lname(self):
        value = self.cleaned_data.get('lname')
        return value.title()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        mail = str(email)
        if mail.endswith('@fladdra.com'):
            return email
        raise forms.ValidationError("Email must end with '@fladdra.com'")

    def clean_mobile(self):
        value = self.cleaned_data.get('mobile')
        if len(str(value)) != 10:
            raise forms.ValidationError('Mobile number must be 10 digit!')
        else:
            return int(value)

    def clean_empid(self):
        value = self.cleaned_data.get('empid')
        if int(value) < 100 or int(value) > 999:
            raise forms.ValidationError('Empid must be a 3 digit number!')
        else:
            return value
    
    def clean_position(self):
        value = str(self.cleaned_data.get('position'))
        pos_list = ['Intern', 'Senior Developer', 'Junior Developer', 'HR', '-', 'test', 'Test']
        if value in pos_list:
            return value.title()
        else:
            raise forms.ValidationError('This position is not valid!')
            
