from django.db import models
from django.db.models.fields import EmailField

# Create your models here.
class Employ:
    empid = models.IntegerField()
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    email = models.EmailField()
    mobile = models.CharField(max_length=10)
    position = models.CharField(max_length=30)