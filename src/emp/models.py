from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import IntegerField
from django.urls import reverse
from datetime import date
from .validators import validate_employID, validate_fname, validate_lname, validate_mobile, validate_fladdraEmail, validate_position
from django.conf import settings
from django.db.models.signals import post_save

class EmployManager(models.Manager): #custom model manager

    def get_queryset(self):
        return super().get_queryset()

    def unarchived(self): 
        '''
        Use this one to get the Un Archived Records
        '''
        return self.get_queryset().filter(is_archived=False)


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
    fladdraEmail = models.EmailField('Fladdra Email', validators=[validate_fladdraEmail, ])
    mobile = models.IntegerField('Mobile No', unique=True, validators=[validate_mobile, ])
    position = models.CharField('Position', max_length=16,choices=position_choices, validators=[validate_position, ])
    github = models.CharField('Github', max_length=50)
    education = models.CharField('Highest Education', max_length=80)
    address = models.TextField('Address')
    joinedOn = models.DateField('Joined On', default=date.today)
    is_archived = models.BooleanField(default=False)
    objects = EmployManager()


    def get_absolute_url(self):   #After create, update, delete it will redirect to this url
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


'''
TAKEN FROM OFFICIAL DOCUMENTATION
'''
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class MyUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username = username,
            email=self.normalize_email(email),
            # userType = userType,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            username,
            email,
            password=password,
        )
        user.userType = 'Admin'
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):

    USER_TYPES = (
        ('Regular', 'Regular'),
        ('Admin', 'Admin'),
        ('Staff', 'Staff'),
        ('Client', 'Client')
    )
    username = models.CharField(max_length=120, unique=True)
    email = models.EmailField(
        verbose_name='Email',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    userType = models.CharField(max_length=8, choices=USER_TYPES, default='Regular')

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'userType']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True


def user_post_save(sender, instance, created, *args, **kwargs):
    if created:         
            Profile.objects.create(user=instance)

post_save.connect(user_post_save, sender=MyUser)

class Profile(models.Model):
    USER_TYPES = (
        ('Regular', 'Regular'),
        ('Admin', 'Admin'),
        ('Staff', 'Staff'),
        ('Client', 'Client')
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    city = models.CharField(max_length=120, null=True, blank=True)
    userType = models.CharField(max_length=8, choices=USER_TYPES, default='Regular')

    def __str__(self):
        return str(self.user.username)


def client_post_save(sender, instance, created, *args, **kwargs):
    if created:
        username = (instance.clientName + str(instance.clientID)).replace(' ' , '')
        MyUser.objects.create(username=username, email=instance.clientEmail, userType='Client', password=username)
        

class Client(models.Model):
    clientID = models.AutoField(primary_key=True)
    clientName = models.CharField('Client Name', max_length=40)
    clientAddress = models.TextField('Client Address')
    clientEmail = models.EmailField('Client Email')

    def __str__(self):
        return str(self.clientName)


post_save.connect(client_post_save, sender=Client)
