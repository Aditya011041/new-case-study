from rest_framework import serializers
from .models import LeaveApplication , LeaveSummary , LeaveType

class LeaveApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveApplication
        fields = '__all__'

class LeaveSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveSummary
        fields = '__all__'

class LeaveTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveType
        fields = '__all__'
