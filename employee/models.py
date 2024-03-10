from django.db import models
from role.models import Role
from department.models import Departments
from designation.models import Designation

# Create your models here.

class Employee(models.Model):
    username = models.CharField(max_length=500, unique=True)
    firstname = models.CharField(max_length=500)
    lastname = models.CharField(max_length=500)
    emp_id = models.CharField(max_length=500, unique=True)
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE)
    department_id = models.ForeignKey(Departments, on_delete=models.CASCADE)
    designation_id = models.ForeignKey(Designation, on_delete=models.CASCADE)
    email = models.CharField(max_length=500)
    phone = models.CharField(max_length=500)
    dob = models.DateField()
    nid = models.CharField(max_length=500)
    gender = models.CharField(max_length=500)
    blood_group = models.CharField(max_length=500)
    emp_status = models.CharField(max_length=500)
    joining_date = models.DateTimeField()
    ending_date = models.DateTimeField(default=None, null=True)
    address = models.TextField()
    photo = models.ImageField(upload_to='media/', default='No images')

    def __str__(self):
        return self.username
    
    
    
    
