from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Departments
from django.contrib import messages
from auth_user.models import User

def departmentpage(request):
    all_userdata = User.objects.select_related('role_id').all()
    data = {"user_data": all_userdata}
    return render(request,'department.html', data)

def department_insert(request):
    department = request.POST.get('department')

    if not department:
        messages.error(request, 'The field cannot be empty')
    else:
        department_obj, created = Departments.objects.get_or_create(name=department)

        if created:
            messages.success(request, 'User Role created successfully')
        else:
            messages.success(request, 'User Role Already Existed')

    return redirect('departmentoutput')


def departmentoutput(request):
    all_data = Departments.objects.all()
    all_userdata = User.objects.select_related('role_id').all()
    if(len(all_data)==0):
        status = False
    else:
        status = True
        
    msg = messages.get_messages(request)
    data = {"department_data": all_data,"user_data": all_userdata, 'status': status, 'msg': msg}
    return render(request,'department.html', data)


def department_edit(request, id):
    all_data = Departments.objects.get(id=id)
    all_userdata = User.objects.select_related('role_id').all()
    data = {"department_data": all_data,"user_data": all_userdata}
    return render(request,'departmentupdate.html', data)

def updatedepartment(request):
    id = request.POST.get('id')
    name = request.POST.get('department')
    
    department_obj = get_object_or_404(Departments, id=id)
    department_obj.name = name
    department_obj.save()
    return redirect('departmentoutput')

def delete_department(request, id):
    department_obj = get_object_or_404(Departments, id=id)
    department_obj.delete()
    return redirect('departmentoutput')
