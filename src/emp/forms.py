from django import forms
from django.contrib.auth.models import User
from django.db.models import fields
from .models import Employ, MyUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError


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
            # 'joinedOn'      #join date will be generated automatically
        ]


class RegistrationForm(UserCreationForm):
    ADMIN = 'admin'
    REGULAR = 'regular'
    STAFF = 'staff'

    USERCHOICES = (
        (ADMIN, 'Admin'),
        (REGULAR, 'Regular'),
        (STAFF, 'Staff')
    )

    email = forms.EmailField(required=True) #this field was already in the UserCreationForm but was'nt compulsory, now it is made required=True
    userType = forms.ChoiceField(required=True, choices=USERCHOICES)  #added this field manually in the Registrationform
    
    class Meta:
        model = User
        fields = [
            'username' , #already in UserCreationForm
            'first_name',   #already in UserCreationForm
            'last_name',    #already in UserCreationForm
            'email',    #overidden
            'userType',  #manually added
            'password1',    #already in UserCreationForm
            'password2'   #already in UserCreationForm         
            ]

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        '''
        This method is called because RegistrationForm is inheriting from UserCreationForm which will take the remaining inputs i.e. username, password1 and password2
        '''
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.userType = self.cleaned_data['userType']

        if commit:
            user.save()

        return user


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ('email', 'username', 'userType')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = MyUser
        fields = ('email', 'password', 'username', 'userType', 'is_active', 'is_staff', 'is_admin')
