from django.shortcuts import render
from rest_framework.views import APIView
from projects.serializers import ProjectSerializer
from projectmanager.models import ProjManager
from projects.models import Project
from projectmanager.serializers import ProjManagerSerializer
from rest_framework.response import Response
from employees.models import Employee
from employees.serializers import EmployeeSerializer

class ManagerView(APIView):
    def get(self, request,  format=None):
        managers = ProjManager.objects.all()
        manager_data = []
        for manager in managers:
            manager_serializer = ProjManagerSerializer(manager)
            projects = Project.objects.filter(managers=manager)
            employees = Employee.objects.filter(project__in=projects).distinct()
            employee_serializer = EmployeeSerializer(employees, many=True)
            manager_data.append({
                'manager': manager_serializer.data,
                'employees': employee_serializer.data
            })
        return Response(manager_data)

class OneManagerView(APIView):
    def get(self, request, pk, format=None):
        manager = ProjManager.objects.get(pk = pk)
        manager_detail =[]
        manager_serializer = ProjManagerSerializer(manager)
        project = Project.objects.filter(managers = manager)
        projects_under_manager = ProjectSerializer(project, many=True)
        employees = Employee.objects.filter(project__in=project).distinct()
        employee_serializer = EmployeeSerializer(employees, many=True)
        manager_detail.append({
           'manager': manager_serializer.data,
            'employees': employee_serializer.data,
            'projects': projects_under_manager.data
        })
        return Response(manager_detail)