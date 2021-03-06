# Generated by Django 3.1.4 on 2021-02-25 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20210225_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeAttendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendance', models.CharField(max_length=100)),
                ('date', models.CharField(blank=True, default='25/02/2021', max_length=100)),
                ('emp_name', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.employee')),
            ],
        ),
    ]
