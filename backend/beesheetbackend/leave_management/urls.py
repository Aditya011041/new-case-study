from django.contrib import admin
from django.urls import path
from . views import LeaveApplicationList , LeaveSummaryDetail , LeaveTypeDetail

urlpatterns = [
    path('leaveapplicationlist/' , LeaveApplicationList.as_view()),
    path('leaveapplicationlist/<int:pk>/', LeaveApplicationList.as_view()),
    path('leaveSummary/<int:pk>/', LeaveSummaryDetail.as_view()),
    path('leaveTypeDetail/', LeaveTypeDetail.as_view()),
    path('leaveTypeDetail/<int:pk>', LeaveTypeDetail.as_view()),
]
