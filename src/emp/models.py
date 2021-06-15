# from django.core.exceptions import ValidationError
# from typing_extensions import Required
from django.db import models
from django.db.models.fields import EmailField, IntegerField
# from django.http.response import HttpResponseRedirect
from django.urls import reverse
# from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect
# from django.core.validators import MaxValueValidator, MinValueValidator
# from django.core.exceptions import ValidationError
from django.db.models.signals import pre_save, post_save
from datetime import date, datetime

# def clean_empid(empid):
#     if empid < 100 and empid > 999:
#         return forms.ValidationError('Empid cannot be greater than 9999!')
#     return empid

# def empid_creater(sender, instance, *args, **kwargs):
#     count = Employ.objects.count()
#     empid = count+1
#     return empid

# pre_save.connect(empid_creater, sender=Employ)


class Employ(models.Model):
    intern = 'Intern'
    sendev = 'Senior Developer'
    jundev = 'Junior Developer'
    hr = 'HR'
    no = '-'
    test = 'Test'
    
    position_choices = [
                (intern ,'Intern'),
                (sendev ,'Senior Developer'),
                 (jundev ,'Junior Developer'),
                 (hr , 'HR'),
                 (no , '-'),
                 (test , 'Test')
                 ]

    #default value for required is True 

    empid = models.AutoField(primary_key=True)
    employID = IntegerField('Employ ID', unique=True)
    fname = models.CharField('First Name', max_length=20)
    lname = models.CharField('Last Name', max_length=20)
    personalEmail = models.EmailField('Personal Email')
    fladdraEmail = models.EmailField('Fladdra Email')
    mobile = models.IntegerField('Mobile No', unique=True)
    position = models.CharField('Position', max_length=16,choices=position_choices)
    # position = models.CharField(max_length=20, null=True)
    github = models.CharField('Github', max_length=50)
    education = models.CharField('Highest Education', max_length=80)
    address = models.TextField('Address')
    joinedOn = models.DateField('Joined On', default=date.today)
    # resume = models.FileField('Upload Resume', upload_to='')



    def get_absolute_url(self):
        return reverse('emp:list_emp')

    def get_delete_url(self):
        return reverse('emp:delete_emp', kwargs = {'empid' : self.empid})

    def get_update_url(self):
        return reverse('emp:update_emp', kwargs = {'empid' : self.empid})

    def get_view_url(self):
        return reverse('emp:view_emp', kwargs = {'empid' : self.empid})

    def get_github_url(self):
        link = 'https://github.com/' + self.github
        return link

    def get_full_name(self):
        return self.fname + ' ' + self.lname

    def __str__(self):
        return "{} - {} - {}".format(self.get_full_name(), self.empid, self.position)


    class Meta: 
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

