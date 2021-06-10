from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.fields import EmailField
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError


def validate_empid(value):
    if value > 9999:
        return ValidationError('Empid cannot be greater than 9999!')


class Employ(models.Model):
    empid = models.IntegerField(validators=[validate_empid, ])
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.EmailField()
    mobile = models.CharField(max_length=10)
    position = models.CharField(max_length=20)

    def get_delete_url(self):
        return reverse('emp:delete_emp', kwargs = {'id' : self.id})

    def get_update_url(self):
        return reverse('emp:update_emp', kwargs = {'id' : self.id})

    def get_absolute_url(self):
        return reverse('emp:view_emp', kwargs = {'id' : self.id})



    def get_full_name(self):
        return self.fname + self.lname

    def __str__(self):
        return "{} : {} : {}".format(self.get_full_name(), self.empid, self.position)


    class Meta: 
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'