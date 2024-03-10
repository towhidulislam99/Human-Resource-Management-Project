from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import Employee
from django.contrib import messages
from auth_user.models import User
from role.models import Role
from department.models import Departments
from employee.models import Employee
from designation.models import Designation
from .models import Leave
from datetime import datetime
import re
import os


def leaveindex(request):
    all_employee = Employee.objects.all().order_by('pk')
    if len(all_employee) == 0:
        status = False
    else:
        status = True
    data = {"employee_data": all_employee, 'status': status}
    return render(request,'leaveapplication.html', data)
     

def leavepage(request):
    if request.method == 'POST':
        applicant_name = request.POST.get('applicant_name')
        leave_reason = request.POST.get('leave_reason')
        start_date_str = request.POST.get('start_date')  # Get start_date as string
        end_date_str = request.POST.get('end_date')      # Get end_date as string

        # Check if start_date_str and end_date_str are not empty before conversion
        if start_date_str and end_date_str:
            # Convert start_date_str and end_date_str to datetime objects
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
        else:
            # Handle the case when start_date or end_date is not provided
            # You can choose to raise an error, redirect the user, or handle it differently based on your requirements
            # For now, we'll just return an error message
            return render(request, 'error.html', {'message': 'Start date or end date is missing'})

        current_datetime = datetime.now()
        
        # Get Employee object using the applicant_name
        employee = Employee.objects.get(pk=applicant_name)

        # Create or update Leave object
        leave_obj, created = Leave.objects.get_or_create(
            applicant_name=employee,
            leave_reason=leave_reason,
            apply_date=current_datetime,
            start_date=start_date,
            end_date=end_date
        )
       
    return render(request, 'leaveapplication.html')


# @login_required
def leave_list(request):
    leaves = Leave.objects.all().select_related('applicant_name')
    print(f'This is The Leaves Data Here: {leaves}')
    return render(request, 'leavelistdatatable.html', {'leaves': leaves})

def leave_view(request, id):
    leaves = Leave.objects.all().select_related('applicant_name').get(id=id) 
    data = {
        'leaves_data': leaves,
    }
    return render(request, 'leaveview.html', data)

def leave_edit(request, id):
    leaves = Leave.objects.all().select_related('applicant_name').get(id=id) 
    all_employee = Employee.objects.all()
    data = {
        'leaves_data': leaves,
        'all_employee': all_employee
    }
    return render(request, 'leaveupdate.html', data)

def leave_update(request):
    id = request.POST.get('id')
    applicant_name_id = request.POST.get('applicant_name')
    leave_reason = request.POST.get('leave_reason')
    start_date_str = request.POST.get('start_date')  # Get start_date as string
    end_date_str = request.POST.get('end_date')      # Get end_date as string
    
    # Convert start_date_str and end_date_str to datetime objects
    start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
    end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
    
    leave_obj = get_object_or_404(Leave, id=id)
    employee_obj = get_object_or_404(Employee, id=applicant_name_id)
    
    leave_obj.applicant_name = employee_obj
    leave_obj.leave_reason = leave_reason
    leave_obj.start_date = start_date
    leave_obj.end_date = end_date
    leave_obj.save()
    return redirect('leave_list')

def leave_delete(request, id):
    leave_obj = get_object_or_404(Leave, id=id)
    leave_obj.delete()
    return redirect('leave_list')

      
def change_leave_status(request, leave_id, new_status):
    # Retrieve the Leave object based on the leave_id
    leave = get_object_or_404(Leave, pk=leave_id)

    # Update the status of the leave object
    leave.status = new_status
    leave.save()

    # Redirect to a specific URL after updating the status
    return redirect('leave_list')  # Redirect to the leave list page or any other page

def appoved_user(request):
    all_appovedleave = Leave.objects.filter(status='Approved').select_related('applicant_name')
    msg = messages.get_messages(request)
    data = {"all_appovedleave": all_appovedleave, 'msg': msg}
    messages.success(request, 'Employee Data Updated successfully')
    return render(request,'leaveapprovedemployeelist.html', data) 

def reject_user(request):
    all_rejectleave = Leave.objects.filter(status='Rejected').select_related('applicant_name')
    msg = messages.get_messages(request)
    data = {"all_rejectleave": all_rejectleave, 'msg': msg}
    messages.success(request, 'Employee Data Updated successfully')
    return render(request,'leaverejectemployeelist.html', data) 
    

# # @login_required
# def leave_approval(request):
#     if request.method == 'POST':
#         # Get the leave ID and status from the request.POST dictionary
#         leave_id = request.POST.get('id')
#         status = request.POST.get('status')
        
#         # Get the leave object associated with the ID
#         leave = Leave.objects.get(id=leave_id)
        
#         # Update the status of the leave object
#         leave.status = status
#         leave.save()

#         # Redirect to the leave list page after updating the status
#         return redirect('leave_list')
#     else:
#         # If the request method is not POST, render the leave_approval.html template
#         return render(request, 'leave_approval.html')









