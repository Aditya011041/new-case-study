from rest_framework import serializers
from projects.serializers import ProjectSerializer
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__' 

# class CombinedSerializer(serializers.Serializer):
#     employees = EmployeeSerializer(many=True)
#     projects = ProjectSerializer(many=True)