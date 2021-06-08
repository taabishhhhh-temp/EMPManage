# Generated by Django 3.2.4 on 2021-06-08 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employ',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='employ',
            name='empid',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='employ',
            name='mobile',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]