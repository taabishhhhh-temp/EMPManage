# from django.db.models.signals import pre_save, post_save
from django.db import models
from django.db.models.fields import IntegerField
from django.urls import reverse
from datetime import date

from .validators import validate_employID, validate_fname, validate_lname, validate_mobile, validate_fladdraEmail, validate_position

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

    empid = models.AutoField(primary_key=True)
    employID = IntegerField('Employ ID', unique=True, validators=[validate_employID, ])  
    fname = models.CharField('First Name', max_length=20, validators= [validate_fname, ])
    lname = models.CharField('Last Name', max_length=20, validators=[validate_lname, ])
    personalEmail = models.EmailField('Personal Email')
    fladdraEmail = models.EmailField('Fladdra Email', validators=[validate_fladdraEmail])
    mobile = models.IntegerField('Mobile No', unique=True, validators=[validate_mobile, ])
    position = models.CharField('Position', max_length=16,choices=position_choices, validators=[validate_position])
    github = models.CharField('Github', max_length=50)
    education = models.CharField('Highest Education', max_length=80)
    address = models.TextField('Address')
    joinedOn = models.DateField('Joined On', default=date.today)
    is_archived = models.BooleanField(default=False, null=True, blank=True)
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
        return 'https://github.com/' + self.github

    def get_full_name(self):
        return self.fname + ' ' + self.lname

    def __str__(self):
        return "{} - {} - {}".format(self.get_full_name(), self.empid, self.position)

    class Meta: 
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'


# def empid_creater(sender, instance, *args, **kwargs):
#     count = Employ.objects.count()
#     empid = count+1
#     return empid

# pre_save.connect(empid_creater, sender=Employ)