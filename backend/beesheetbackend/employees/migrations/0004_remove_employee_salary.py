# Generated by Django 5.0.1 on 2024-03-06 03:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_alter_employee_salary'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='salary',
        ),
    ]
