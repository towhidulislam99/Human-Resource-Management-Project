from django.db import models
from django.utils import timezone
from employee.models import Employee
from datetime import datetime
from django.core.exceptions import ValidationError

# Create your models here.

class Attendance(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    attendence_date = models.DateField(auto_now_add=True)
    signin_time = models.DateTimeField()
    signout_time = models.DateTimeField(null=True, blank=True)
    working_hour = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    
  
    # def save(self, *args, **kwargs):
    # # Update the signin_time field with the current date and time if it's not already set
    #     if not self.signin_time:
    #         self.signin_time = timezone.now()
            
    #     # Call the original save() method to save the instance
    #     super(Attendance, self).save(*args, **kwargs)
        
       
    def save(self, *args, **kwargs):
        # Call the original save() method to save the instance
        super(Attendance, self).save(*args, **kwargs)

        # Calculate total hours if both signin_time and signout_time are present
        if self.signin_time and self.signout_time:
            time_difference = self.signout_time - self.signin_time
            total_hours = time_difference.total_seconds() / 3600  # Convert seconds to hours
            self.working_hour = round(total_hours, 2)  # Round to 2 decimal places

            # Update the total_hours field in the database
            Attendance.objects.filter(pk=self.pk).update(working_hour=self.working_hour)