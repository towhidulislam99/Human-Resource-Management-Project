from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Employee
from django.contrib import messages
from auth_user.models import User
from role.models import Role
from department.models import Departments
from designation.models import Designation
from diciplinary.models import Diciplinary
import re
import os

def diciplinarypage(request):
    all_employee = Employee.objects.all().order_by('pk')
    all_department = Departments.objects.all().order_by('pk')
    all_designation = Designation.objects.all().order_by('pk')
    if len(all_employee) == 0 and len(all_department) == 0 and len(all_designation) == 0:
        status = False
    else:
        status = True
    data = {"employee_data": all_employee, "department_data": all_department, "designation_data": all_designation, 'status': status}
    return render(request,'diciplinary.html', data)

def diciplinary_insert(request):
    if request.method == 'POST':
        employee_id = request.POST.get('employee_id')
        dept_id = request.POST.get('dept_id')
        desig_id = request.POST.get('desig_id')
        emp_personal_id = request.POST.get('emp_personal_id')
        date_of_diciplinary = request.POST.get('date_of_diciplinary')
        diciplinary_reason_name = request.POST.get('diciplinary_reason_name')
        description = request.POST.get('description')
        
        department = Departments.objects.get(pk=dept_id)
        designation = Designation.objects.get(pk=desig_id)
        employee = Employee.objects.get(pk = employee_id)
        
        diciplinary_obj, created = Diciplinary.objects.get_or_create(
                employee_id=employee, 
                dept_id=department, 
                desig_id=designation, 
                emp_personal_id=emp_personal_id,
                date_of_diciplinary = date_of_diciplinary,
                diciplinary_reason_name = diciplinary_reason_name,
                description =description
        )

        if created:
                messages.success(request, 'Employee Data created successfully')
        else:
                messages.success(request, 'Employee Already Existed')

        return redirect('diciplinarypage')

          
def diciplinaryoutput(request):
    all_userdata = Diciplinary.objects.select_related('employee_id', 'dept_id', 'desig_id').all()
    if(len(all_userdata)==0):
        status_u = False
    else:
        status_u = True
        
    msg = messages.get_messages(request)
    data = {"diciplinary_data": all_userdata, 'status_u': status_u, 'msg': msg}
    return render(request,'diciplinarydatatable.html', data)


def diciplinary_edit(request, id):
    diciplinary_data = Diciplinary.objects.select_related('employee_id', 'dept_id', 'desig_id').get(id=id)
    
    print(diciplinary_data.dept_id)
    all_employee = Employee.objects.all()
    all_department = Departments.objects.all()
    print(all_department)
    for department in all_department:
        if diciplinary_data.dept_id.id == department.id:
            print("Get this Value")
            print(department.name)
    all_designation = Designation.objects.all()
    msg = messages.get_messages(request)
    data = {'diciplinary_data': diciplinary_data, 'msg': msg, 'all_employee': all_employee , 'all_department' : all_department, 'all_designation' : all_designation}
    messages.success(request, 'Employee Data Updated successfully')
    return render(request,'diciplinaryupdate.html', data)

def diciplinary_update(request):
    id = request.POST.get('id')
    employee_id = request.POST.get('employee_id')
    dept_id = request.POST.get('dept_id')
    desig_id = request.POST.get('desig_id')
    emp_personal_id = request.POST.get('emp_personal_id')
    date_of_diciplinary = request.POST.get('date_of_diciplinary')
    diciplinary_reason_name = request.POST.get('diciplinary_reason_name')
    description = request.POST.get('description')
   
    diciplinary_obj = get_object_or_404(Diciplinary, id=id)
    employee_obj = get_object_or_404(Employee, id=employee_id)
    department_obj = get_object_or_404(Departments, id=dept_id)
    designation_obj = get_object_or_404(Designation, id=desig_id)
    
     
    # role_obj = Role.objects.get(id=role_id)
    # user_obj.role_id = role_obj
    diciplinary_obj.employee_id = employee_obj
    diciplinary_obj.dept_id = department_obj
    diciplinary_obj.desig_id = designation_obj
    diciplinary_obj.emp_personal_id = emp_personal_id
    diciplinary_obj.date_of_diciplinary = date_of_diciplinary
    diciplinary_obj.diciplinary_reason_name = diciplinary_reason_name
    diciplinary_obj.description = description
    diciplinary_obj.save()
    return redirect('diciplinaryoutput')

def diciplinary_delete(request, id):
    diciplinary_obj = get_object_or_404(Diciplinary, id=id)
    diciplinary_obj.delete()
    return redirect('diciplinaryoutput')





