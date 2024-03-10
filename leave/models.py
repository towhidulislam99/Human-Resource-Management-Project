from django.db import models
from employee.models import Employee
from designation.models import Designation
from datetime import timedelta
from datetime import datetime

# Create your models here.

class Leave(models.Model):
    PENDING = 'Pending'
    APPROVED = 'approved'
    REJECTED = 'rejected'
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (APPROVED, 'Approved'),
        (REJECTED, 'Rejected'),
    ]

    applicant_name = models.ForeignKey(Employee, on_delete=models.CASCADE)
    leave_reason = models.TextField()
    apply_date = models.DateTimeField(auto_now_add=True)
    start_date = models.DateField()
    end_date = models.DateField()
    leave_days = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PENDING)
    
    def save(self, *args, **kwargs):
        # Calculate the difference between end_date and start_date
        delta = self.end_date - self.start_date

        # Assign the number of days to leave_days
        self.leave_days = delta.days + 1

        # Call the original save() method to save the instance
        super(Leave, self).save(*args, **kwargs)
        
        
    
    
    
    
    
