# from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.fields import EmailField, IntegerField
from django.urls import reverse
# from django.core.validators import MaxValueValidator, MinValueValidator
# from django.core.exceptions import ValidationError
from django.db.models.signals import pre_save, post_save

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

    empid = models.AutoField(primary_key=True)
    employID = IntegerField('Employ ID')
    fname = models.CharField('First Name', max_length=20)
    lname = models.CharField('Last Name', max_length=20)
    personalEmail = models.EmailField('Personal Email')
    fladdraEmail = models.EmailField('Fladdra Email')
    mobile = models.IntegerField('Mobile No', default=None)
    position = models.CharField('Position' , max_length=16, choices=position_choices)
    # position = models.CharField(max_length=20, null=True)
    github = models.CharField('Github', max_length=50, )
    education = models.TextField('Highest Education')
    address = models.TextField('Address')


    def get_delete_url(self):
        return reverse('emp:delete_emp', kwargs = {'empid' : self.empid})

    def get_update_url(self):
        return reverse('emp:update_emp', kwargs = {'empid' : self.empid})

    def get_absolute_url(self):
        return reverse('emp:view_emp', kwargs = {'empid' : self.empid})

    # def get_github_url(self):
    #     return reverse('emp:github_emp', kwargs={'EMPID' : self.empid})

    def get_full_name(self):
        return self.fname + self.lname

    def __str__(self):
        return "{} : {} : {}".format(self.get_full_name(), self.empid, self.position)


    class Meta: 
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

