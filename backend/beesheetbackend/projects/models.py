from django.db import models
from employees.models import Employee
from projectmanager.models import ProjManager
from django.db.models.signals import post_save
from django.dispatch import receiver



class Project(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(auto_now=True)
    assigned_to = models.ManyToManyField(Employee, blank=True)
    managers = models.ManyToManyField(ProjManager , related_name='projects')
    # , related_name='projects'

    def __str__(self):
        return self.title
# @receiver(post_save, sender=Project)
# def update_managers_with_assigned_employees(sender, instance, created, **kwargs):
#     if created:
#         for employee in instance.assigned_to.all():
#             for manager in instance.managers.all():
#                 manager.employees.add(employee)