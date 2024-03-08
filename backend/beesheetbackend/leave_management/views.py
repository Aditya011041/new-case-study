from django.shortcuts import render
from rest_framework.views import APIView
from leave_management.serializers import LeaveApplicationSerializer , LeaveSummarySerializer , LeaveTypeSerializer
from leave_management.models import LeaveApplication, LeaveSummary , LeaveType
from rest_framework.response import Response

# Create your views here. 

class LeaveApplicationList(APIView):
    def get(self, request,pk, format=None):
        leave_applications = LeaveApplication.objects.get(pk=pk)
        serializer = LeaveApplicationSerializer(leave_applications, many=True)
        return Response(serializer.data)
    
    def post(self, request , pk):
        request.data['employee'] = pk
        serializer = LeaveApplicationSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400) 
    
    def delete(self,request , pk):
        leave_application = LeaveApplication.objects.get(pk=pk)
        leave_application.delete()
        return Response(status=204)
    

class LeaveSummaryDetail(APIView):
    def get(self,request,pk):
        brief = LeaveSummary.objects.get(pk=pk)
        serializer = LeaveSummarySerializer(brief)
        return Response(serializer.data)
    
class LeaveTypeDetail(APIView):
    def get(self,request):
        leave_types = LeaveType.objects.all()
        serializer = LeaveTypeSerializer(leave_types, many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = LeaveTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def put(self,request,pk):
        leave_id = LeaveType.objects.get(pk = pk)
        serializer = LeaveTypeSerializer(leave_id, data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

        

from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=LeaveApplication)
def create_leave_report(sender,instance , created , **kwargs):
    if created:
       employee = instance.employee
       leave_type = instance.leave_type
       total_allocated_days = leave_type.days_allocated
       total_used_days = LeaveApplication.objects.filter(employee=employee , leave_type=leave_type).count()
       total_available_days = total_allocated_days - total_used_days

       leave_report = LeaveSummary.objects.create()
       leave_report.employee.set([employee])
       leave_report.total_available = total_available_days
       leave_report.total_used  = total_used_days
       leave_report.save()