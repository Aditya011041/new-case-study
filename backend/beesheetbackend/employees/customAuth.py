from django.contrib.auth.backends import ModelBackend
from employees.models import Employee
from projectmanager.models import ProjManager

class EmailOrUsernameModelBackend(ModelBackend):
    def authenticate(self, request, email=None, **kwargs):
        user = None

        if email:
            employee = Employee.objects.filter(email=email).first()
            if employee:
                user = employee
            else:
                manager = ProjManager.objects.filter(email=email).first()
                if manager:
                    user = manager

        return user
