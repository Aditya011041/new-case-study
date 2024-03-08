from rest_framework import serializers
from .models import ProjManager
from employees.serializers import EmployeeSerializer
from projects.serializers import ProjectSerializer

class ProjManagerSerializer(serializers.ModelSerializer):
    # projects = ProjectSerializer(many=True)
    # employees = EmployeeSerializer(many=True)
    class Meta:
        model = ProjManager
        fields = ['id' , 'name' , 'email']