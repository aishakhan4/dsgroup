# Generated by Django 3.1.4 on 2021-02-26 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_staffattendance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffattendance',
            name='staff_name',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.staff'),
        ),
    ]
