# Generated by Django 3.1.4 on 2021-02-25 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_employeeattendance'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='Profile',
            new_name='profile',
        ),
    ]
