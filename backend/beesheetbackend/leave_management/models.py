from django.db import models
from employees.models import Employee

class LeaveType(models.Model):
    CASUAL = 'Casual'
    SICK = 'Sick'
    EMERGENCY = 'Emergency'
    WFH = 'Work from Home'

    LEAVE_TYPE_CHOICES = [
        (CASUAL, 'Casual'),
        (SICK, 'Sick'),
        (EMERGENCY, 'Emergency'),
        (WFH, 'Work from Home'),
    ]

    name = models.CharField(max_length=100, choices=LEAVE_TYPE_CHOICES)
    days_allocated = models.PositiveIntegerField()


    def __str__(self):
        return self.name
class LeaveApplication(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    leave_type = models.ForeignKey(LeaveType, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, default='PENDING')

    def __str__(self):
        return f"{self.employee.name} - {self.leave_type.name}"

class LeaveSummary(models.Model):
    employee = models.ManyToManyField(Employee)
    total_available = models.PositiveIntegerField(default=0)
    total_used = models.PositiveIntegerField(default=0)

    

