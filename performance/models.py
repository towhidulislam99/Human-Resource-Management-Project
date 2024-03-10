from django.db import models
from django.utils import timezone
from employee.models import Employee
from datetime import datetime
from django.core.exceptions import ValidationError

# Create your models here.

class Performance(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    review_date = models.DateField(auto_now_add=True)
    rating = models.FloatField()  # Assuming rating is an integer field
    comments = models.TextField(null=True, blank=True)  # Assuming comments is a text field
   
    
  
   