from django.db import models
from role.models import Role
from department.models import Departments
from designation.models import Designation
from employee.models import Employee

# Create your models here.

class Diciplinary(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    dept_id = models.ForeignKey(Departments, on_delete=models.CASCADE)
    desig_id = models.ForeignKey(Designation, on_delete=models.CASCADE)
    emp_personal_id =  models.CharField(max_length=500)
    date_of_diciplinary = models.DateField()
    diciplinary_reason_name = models.CharField(max_length=500)
    description = models.TextField()
    
    
    # username = models.CharField(max_length=500, unique=True)
    # firstname = models.CharField(max_length=500)
    # lastname = models.CharField(max_length=500)
    # emp_id = models.CharField(max_length=500, unique=True)
    # role_id = models.ForeignKey(Role, on_delete=models.CASCADE)
    # department_id = models.ForeignKey(Departments, on_delete=models.CASCADE)
    # designation_id = models.ForeignKey(Designation, on_delete=models.CASCADE)
    # email = models.CharField(max_length=500)
    # phone = models.CharField(max_length=500)
    # dob = models.DateField()
    # nid = models.CharField(max_length=500)
    # gender = models.CharField(max_length=500)
    # blood_group = models.CharField(max_length=500)
    # emp_status = models.CharField(max_length=500)
    # joining_date = models.DateTimeField()
    # ending_date = models.DateTimeField(default=None, null=True)
    # address = models.TextField()
    # photo = models.ImageField(upload_to='media/', default='No images')

    # def __str__(self):
    #     return self.username
    
    
    
    
