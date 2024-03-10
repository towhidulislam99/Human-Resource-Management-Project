from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from auth_user.models import User
from django.shortcuts import render
from django.http import JsonResponse
from .models import Attendance
from .models import Employee
from django.utils import timezone
from datetime import date
from datetime import datetime
from django.db.models import Subquery


def attendancepage(request):
    all_employee = Employee.objects.all().order_by('pk')
    if len(all_employee) == 0:
        status = False
    else:
        status = True
    data = {"employee_data": all_employee, 'status': status}
    return render(request,'attendance.html', data)


def attendance_insert(request):
    if request.method == 'POST':
        employee_id = request.POST.get('employee_id')
        
        # Retrieve the Employee instance using the employee_id value
        employee = get_object_or_404(Employee, pk=employee_id)
        
        # Check if attendance already exists for the selected employee on the current date
        existing_attendance = Attendance.objects.filter(employee_id=employee, attendence_date=date.today()).exists()
        if existing_attendance:
            messages.error(request, "Attendance already exists for this employee today.")
            return redirect('attendancepage')  # Redirect to the attendance form page or any other page
            
        # If attendance doesn't exist, create a new attendance entry
        attendance_obj = Attendance(employee_id=employee, signin_time=timezone.now())
        attendance_obj.save()
        
        messages.success(request, "Attendance recorded successfully.")
        return redirect('attendancepage')  # Redirect to the attendance form page or any other page
    
    # If request method is not POST, render the attendance form page
    return render(request, 'attendance.html')


# def attendance_insert(request):
#     if request.method == 'POST':
#         employee_id = request.POST.get('employee_id')
        
#         # Get Employee object using the applicant_name
#         employee = Employee.objects.get(pk=employee_id)

#         # Create or update Leave object
#         attendance_obj, created = Attendance.objects.get_or_create(
#             employee_id = employee,  
#             signin_time = timezone.now()      
#         )
       
#     return render(request, 'attendance.html')

 
def attendance_view(request):
    attendance_data = Attendance.objects.all().select_related('employee_id')
    data = {
        'attendance_data': attendance_data,
    }
    return render(request, 'attendanceview.html', data)

def attendance_list(request):
    attendance_data = Attendance.objects.all().select_related('employee_id')
    data = {
        'attendance_list': attendance_data,
    }
    return render(request, 'attendancelist.html', data)

def attendance_edit(request, id):
    attendance_data = Attendance.objects.all().select_related('employee_id').get(id=id)
    all_employee = Employee.objects.all()
    data = {
        'attendance_list': attendance_data,
        'all_employee': all_employee,
    }
    return render(request, 'attendanceupdate.html', data)

def attendance_update(request):
    id = request.POST.get('id')
    employee_id = request.POST.get('employee_id')
    attendence_date = request.POST.get('attendence_date')
    signin_time_str = request.POST.get('signin_time')
    signout_time_str = request.POST.get('signout_time')
   
    attendance_obj = get_object_or_404(Attendance, id=id)
    employee_obj = get_object_or_404(Employee, id=employee_id)
    
    attendance_obj.employee_id = employee_obj
    attendance_obj.attendence_date = attendence_date
    
    # Convert string representations of time to datetime objects
    if signin_time_str:
        attendance_obj.signin_time = datetime.strptime(signin_time_str, '%Y-%m-%dT%H:%M:%S')
    if signout_time_str:
        attendance_obj.signout_time = datetime.strptime(signout_time_str, '%Y-%m-%dT%H:%M:%S')
    
    attendance_obj.save()
    return redirect('attendance_list')
    
def attendance_delete(request, id):
    attendance_obj = get_object_or_404(Attendance, id=id)
    attendance_obj.delete()
    return redirect('attendance_list')


def signout_view(request, attendance_id):
    attendance = get_object_or_404(Attendance, pk=attendance_id)
    attendance.signout_time = timezone.now()
    attendance.save()
    return redirect('attendance_view')  # Redirect to some view after signing out

def attendance_present(request):
    attendances_with_signout_time = Attendance.objects.exclude(signout_time=None)
    msg = messages.get_messages(request)
    data = {"present_employee": attendances_with_signout_time, 'msg': msg}
    messages.success(request, 'Employee Data Updated successfully')
    return render(request,'attendancepresentlist.html', data) 


def attendance_absent(request):
   # Subquery to get a list of employee IDs with a signout time recorded
    employees_with_signout_time = Attendance.objects.exclude(signout_time=None).values('employee_id')
    print(employees_with_signout_time)

# Query to get all employees who do not have a signout time recorded
    employees_without_signout_time = Employee.objects.exclude(id__in=Subquery(employees_with_signout_time))
    print(f'Total Employee: {employees_without_signout_time}')
    today_date = date.today()
    msg = messages.get_messages(request)
    data = {"absent_employee": employees_without_signout_time, 'today_date': today_date, 'msg': msg}
    messages.success(request, 'Employee Data Updated successfully')
    return render(request,'attendanceabsentlist.html', data) 


     

