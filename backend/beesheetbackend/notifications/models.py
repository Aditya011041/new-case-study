from django.db import models
from employees.models import Employee
from leave_management.models import LeaveApplication

class LeaveNotification(models.Model):
    leave_application = models.ForeignKey(LeaveApplication, on_delete=models.CASCADE)
    recipient = models.ForeignKey(Employee, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True,)

   

    def __str__(self):
        return f'Notification for {self.leave_application} - {self.recipient}'
