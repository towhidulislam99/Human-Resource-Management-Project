from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from auth_user.models import User
from django.shortcuts import render
from django.http import JsonResponse
from attendance.models import Attendance
from .models import Employee
from .models import Performance
from django.utils import timezone
from datetime import date
from datetime import datetime
from django.db.models import Subquery


def performancepage(request):
    all_employee = Employee.objects.all().order_by('pk')
    if len(all_employee) == 0:
        status = False
    else:
        status = True
    data = {"employee_data": all_employee, 'status': status}
    return render(request,'performancepage.html', data)


def performance_insert(request):
    if request.method == 'POST':
        employee_id = request.POST.get('employee_id')
        rating = request.POST.get('rating')
        comments = request.POST.get('comments')
        
        # Retrieve the Employee instance using the employee_id value
        employee = get_object_or_404(Employee, pk=employee_id)
        performance_obj = Performance(employee_id=employee, review_date=date.today(), rating = rating, comments = comments )
        performance_obj.save()
        
        messages.success(request, "Attendance recorded successfully.")
        return redirect('performancepage')  # Redirect to the attendance form page or any other page
    
    # If request method is not POST, render the attendance form page
    return render(request, 'performancepage.html')


def performance_list(request):
    performance_data = Performance.objects.all().select_related('employee_id')
    data = {
        'performance_data': performance_data,
    }
    return render(request, 'performancelist.html', data)


def performance_view(request):
    performance_data = Performance.objects.all().select_related('employee_id')
    data = {
        'performance_data': performance_data,
    }
    return render(request, 'performanceview.html', data)

def performance_edit(request, id):
    performance_data = Performance.objects.all().select_related('employee_id').get(id=id)
    all_employee = Employee.objects.all()
    data = {
        'performance_data': performance_data,
        'all_employee': all_employee,
    }
    return render(request, 'performanceupdate.html', data)


def performance_update(request):
    id = request.POST.get('id')
    employee_id = request.POST.get('employee_id')
    review_date = request.POST.get('review_date')
    rating = request.POST.get('rating')
    comments = request.POST.get('comments')
   
    performance_obj = get_object_or_404(Performance, id=id)
    employee_obj = get_object_or_404(Employee, id=employee_id)
    
    performance_obj.employee_id = employee_obj
    performance_obj.review_date = review_date
    performance_obj.rating = rating
    performance_obj.comments = comments
    performance_obj.save()
    return redirect('performance_view')

def performance_delete(request, id):
    performance_obj = get_object_or_404(Performance, id=id)
    performance_obj.delete()
    return redirect('performance_view')




     

