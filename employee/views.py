from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Employee
from django.contrib import messages
from auth_user.models import User
from role.models import Role
from department.models import Departments
from designation.models import Designation
import re
import os

def employeepage(request):
    all_roles = Role.objects.all().order_by('pk')
    all_department = Departments.objects.all().order_by('pk')
    all_designation = Designation.objects.all().order_by('pk')
    if len(all_roles) == 0 and len(all_department) == 0 and len(all_designation) == 0:
        status = False
    else:
        status = True
    data = {"role_data": all_roles, "department_data": all_department, "designation_data": all_designation, 'status': status}
    return render(request,'employee.html', data)

def employee_insert(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        emp_id = request.POST.get('emp_id')
        role_id = request.POST.get('role_id')
        department_id = request.POST.get('department_id')
        designation_id = request.POST.get('designation_id')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        dob = request.POST.get('dob')
        nid = request.POST.get('nid')
        gender = request.POST.get('gender')
        blood_group = request.POST.get('blood_group')
        emp_status = request.POST.get('emp_status')
        joining_date = request.POST.get('joining_date')
        ending_date = request.POST.get('ending_date')
        address = request.POST.get('address')
        photo = request.FILES.get('photo')
        pattern = r"^[a-zA-Z0-9_.]+@gmail\.com$"
        
        if not all([username, firstname, lastname, emp_id ,role_id, department_id, designation_id, email, phone, dob, nid, gender, blood_group,emp_status, joining_date, ending_date, address, photo]):
            messages.error(request, 'Please fill all the fields')
            return HttpResponse('Please fill all the fields')

        # elif any(len(field) < 3 for field in [fullname, password, confirmpassword]):
        #     messages.error(request, 'Name, Password, and Confirm Password should be at least 3 characters long')
        #     return HttpResponse('Name, Password, and Confirm Password should be at least 3 characters long')

        elif len(phone) != 11:
            messages.error(request, 'Phone Number must be at least 11 digits long')
            return HttpResponse('Phone Number must be at least 11 digits long')
        
        elif len(nid) != 10 and len(nid) != 17:
            messages.error(request, 'NID Number muste at least 10  digits  or 17 Digit long')
            return HttpResponse('Phone Number must be b at least 10 or 17 digits long')

        elif not re.match(pattern, email):
            return HttpResponse('Email is not validated')
        
        else:
            try:
                role_id = int(role_id)  # Convert role_id to integer if it's a string
                department_id = int(department_id) 
                designation_id = int(designation_id)
                role = Role.objects.get(pk=role_id)
                department = Departments.objects.get(pk=department_id)
                designation = Designation.objects.get(pk=designation_id)
                
                employee_obj, created = Employee.objects.get_or_create(
                username=username, 
                firstname=firstname, 
                lastname=lastname, 
                emp_id=emp_id,
                role_id=role,  # Use role_id instead of role
                department_id=department,  # Use department_id instead of department
                designation_id=designation,  # Use designation_id instead of designation
                email=email, 
                phone=phone, 
                dob=dob, 
                nid=nid, 
                gender=gender, 
                blood_group=blood_group, 
               emp_status=emp_status, 
                joining_date=joining_date, 
                ending_date=ending_date, 
                address=address, 
                photo=photo
        )
                
                if created:
                    messages.success(request, 'Employee Data created successfully')
                else:
                    messages.success(request, 'Employee Already Existed')

                return redirect('employeepage')

            except Role.DoesNotExist:
                messages.error(request, 'Role does not exist')
                return HttpResponse('Data Cannot be submitted')
            
            except Departments.DoesNotExist:
                messages.error(request, 'Department does not exist')
                return HttpResponse('Data Cannot be submitted')
            
            except Designation.DoesNotExist:
                messages.error(request, 'Designation does not exist')
                return HttpResponse('Data Cannot be submitted')

    else:
            return HttpResponse('Page Not Found')


# def signuppagedata(request):
#     all_userdata = Employee.objects.select_related('role_id', 'department_id', 'designation_id').all()
#     data = {"user_data": all_userdata}
#     return render(request,'authuserdata.html', data)
          

def employeeoutput(request):
    all_userdata = Employee.objects.select_related('role_id', 'department_id', 'designation_id').all()
    if(len(all_userdata)==0):
        status_u = False
    else:
        status_u = True
        
    msg = messages.get_messages(request)
    data = {"employee_data": all_userdata, 'status_u': status_u, 'msg': msg}
    return render(request,'employeedatatable.html', data)


def employeeview(request, id):
    all_empdata = Employee.objects.filter(id = id).select_related('role_id', 'department_id', 'designation_id')
    msg = messages.get_messages(request)
    data = {"all_emp_data": all_empdata, 'msg': msg}
    messages.success(request, 'Employee Data Updated successfully')
    return render(request,'employeeviewtable.html', data)


def employeelist(request):
    all_empployeelist = Employee.objects.select_related('role_id', 'department_id', 'designation_id').all()
    if(len(all_empployeelist)==0):
        status_u = False
    else:
        status_u = True
        
    msg = messages.get_messages(request)
    data = {"all_emp_list": all_empployeelist, 'status_u': status_u, 'msg': msg}
    return render(request,'employeelist.html', data)


def employee_edit(request, id):
    employee_data = Employee.objects.select_related('role_id', 'department_id', 'designation_id').get(id=id)
    all_roles = Role.objects.all()
    all_department = Departments.objects.all()
    all_designation = Designation.objects.all()
    msg = messages.get_messages(request)
    data = {'emp_data': employee_data, 'msg': msg, 'all_roles': all_roles , 'all_department' : all_department, 'all_designation' : all_designation}
    messages.success(request, 'Employee Data Updated successfully')
    return render(request,'employeeupdate.html', data)

def employeeview_update(request):
    id = request.POST.get('id')
    username = request.POST.get('username')
    firstname = request.POST.get('firstname')
    lastname = request.POST.get('lastname')
    emp_id = request.POST.get('emp_id')
    role_id = request.POST.get('role_id')
    department_id = request.POST.get('department_id')
    designation_id = request.POST.get('designation_id')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    dob = request.POST.get('dob')
    nid = request.POST.get('nid')
    gender = request.POST.get('gender')
    blood_group = request.POST.get('blood_group')
    emp_status = request.POST.get('emp_status')
    joining_date = request.POST.get('joining_date')
    ending_date = request.POST.get('ending_date')
    address = request.POST.get('address')
   

    employee_obj = get_object_or_404(Employee, id=id)
    role_obj = get_object_or_404(Role, id=role_id)
    department_obj = get_object_or_404(Departments, id=department_id)
    designation_obj = get_object_or_404(Designation, id=designation_id)
    
    # Check if new image and video files are provided
    if 'photo' in request.FILES:
        # If a new image is provided, delete the old one if it exists
        if employee_obj.photo:
            os.remove(employee_obj.photo.path)
        employee_obj.photo = request.FILES['photo']
     
    # role_obj = Role.objects.get(id=role_id)
    # user_obj.role_id = role_obj
    employee_obj.username = username
    employee_obj.firstname = firstname
    employee_obj.lastname = lastname
    employee_obj.emp_id = emp_id
    employee_obj.role_id = role_obj
    employee_obj.department_id = department_obj
    employee_obj.designation_id = designation_obj
    employee_obj.email = email
    employee_obj.phone = phone
    employee_obj.dob = dob
    employee_obj.nid = nid
    employee_obj.gender = gender
    employee_obj.blood_group = blood_group
    employee_obj.emp_status = emp_status
    employee_obj.joining_date = joining_date
    employee_obj.ending_date = ending_date
    employee_obj.address = address
    employee_obj.save()
    return redirect('employeeoutput')

def employee_delete(request, id):
    employee_obj = get_object_or_404(Employee, id=id)
    employee_obj.delete()
    return redirect('employeeoutput')

def inactiveuser(request):
    all_inactivedata = Employee.objects.filter(emp_status='Inactive').select_related('role_id', 'department_id', 'designation_id')
    print(all_inactivedata)
    msg = messages.get_messages(request)
    data = {"all_inactivedata": all_inactivedata, 'msg': msg}
    messages.success(request, 'Employee Data Updated successfully')
    return render(request,'inactivelist.html', data) 








