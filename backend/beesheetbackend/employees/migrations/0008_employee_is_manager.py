# Generated by Django 5.0.1 on 2024-03-08 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0007_remove_employee_manager'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='is_manager',
            field=models.BooleanField(default=False),
        ),
    ]
