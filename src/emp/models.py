from django.db import models
from django.db.models.fields import EmailField
from django.urls import reverse

class Employ(models.Model):
    empid = models.IntegerField(unique=True)
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=10, unique=True)
    position = models.CharField(max_length=20)

    def get_absolute_url(self):
        return reverse('EMP:view', kwargs = {'id' : self.id})
