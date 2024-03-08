from rest_framework.views import APIView
from rest_framework.response import Response
from employees.models import Employee
from employees.serializers import EmployeeSerializer
from projectmanager.models import ProjManager
from projectmanager.serializers import ProjManagerSerializer
from projects.models import Project
from projects.serializers import ProjectSerializer
from rest_framework import status
from django.contrib.auth import authenticate
from django.http import JsonResponse


class EmployeeId(APIView):
    def get(self,request):
        employees = Employee.objects.all()
        employee_serializer = EmployeeSerializer(employees, many=True)
        return Response(employee_serializer.data)


class EmpList(APIView):
    def get(self, request, pk, format=None):
        try:
            employee = Employee.objects.get(pk=pk)
            print({employee})
        except Employee.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        employee_serializer = EmployeeSerializer(employee)
        
        
        projects = Project.objects.filter(assigned_to=employee)
        project_serializer = ProjectSerializer(projects, many=True)
        projectsMan = ProjManager.objects.filter(projects__in =projects).distinct()
        projectMan_serializer = ProjManagerSerializer(projectsMan, many=True)
        
        data = {
            'employee': employee_serializer.data,
            'managers': projectMan_serializer.data,
            'projects': project_serializer.data
        }
        return Response(data)
    
 

from django.contrib.auth import authenticate

# class Login(APIView):
#     def post(self, request, format=None):
#         name = request.data.get('name')
#         email = request.data.get('email')
#         user = authenticate(request, name=name, email=email)

#         if user is not None:
#             is_manager = getattr(user, 'is_manager', False)
#             return JsonResponse({'emp_id': user.id, 'is_manager': is_manager})
#         else:
#             return JsonResponse({'error': 'Authentication failed'}, status=400)


            # Determine if the user is a manager or not


class Login(APIView):
    def post(self, request, format=None):
        email = request.data.get('email')
        user = authenticate(request, email=email)

        if user is not None:
            is_manager = isinstance(user, ProjManager)
            manager_ki_id = None
            if is_manager:
                manager_ki_id = user.id
            return JsonResponse({'emp_id': user.id, 'is_manager': is_manager , 'manager_Id' : manager_ki_id})
        else:
            return JsonResponse({'error': 'Authentication failed'}, status=400)