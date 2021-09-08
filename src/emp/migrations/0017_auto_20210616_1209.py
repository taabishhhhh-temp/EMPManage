# Generated by Django 3.2.4 on 2021-06-16 12:09

from django.db import migrations, models
import emp.validators


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0016_auto_20210616_0947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employ',
            name='employID',
            field=models.IntegerField(unique=True, validators=[emp.validators.validate_employID], verbose_name='Employ ID'),
        ),
        migrations.AlterField(
            model_name='employ',
            name='fladdraEmail',
            field=models.EmailField(max_length=254, validators=[emp.validators.validate_fladdraEmail], verbose_name='Fladdra Email'),
        ),
        migrations.AlterField(
            model_name='employ',
            name='fname',
            field=models.CharField(max_length=20, validators=[emp.validators.validate_fname], verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='employ',
            name='lname',
            field=models.CharField(max_length=20, validators=[emp.validators.validate_lname], verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='employ',
            name='mobile',
            field=models.IntegerField(unique=True, validators=[emp.validators.validate_mobile], verbose_name='Mobile No'),
        ),
        migrations.AlterField(
            model_name='employ',
            name='position',
            field=models.CharField(choices=[('Intern', 'Intern'), ('Senior Developer', 'Senior Developer'), ('Junior Developer', 'Junior Developer'), ('HR', 'HR'), ('-', '-'), ('Test', 'Test')], max_length=16, validators=[emp.validators.validate_position], verbose_name='Position'),
        ),
    ]
