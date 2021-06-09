from django.db import models
from django.db.models.fields import EmailField
from django.urls import reverse

class Employ(models.Model):
    empid = models.IntegerField()
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.EmailField()
    mobile = models.CharField(max_length=10)
    position = models.CharField(max_length=20)

    def get_absolute_url(self):
        return reverse('emp:view_emp', kwargs = {'id' : self.id})
