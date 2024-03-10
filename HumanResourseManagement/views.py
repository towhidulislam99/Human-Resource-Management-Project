from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from auth_user.models import User,Role
from attendance.models import Attendance
from employee.models import Employee
from leave.models import Leave

# from .models import User

def indexpage(request):
    all_userdata = User.objects.select_related('role_id').all()
    all_employee = Employee.objects.all().count()
    all_pending_leave = Leave.objects.filter(status='Pending').count()
    attendances_with_signout_time_all = Attendance.objects.exclude(signout_time=None).count()
    print(f'All Employee For This Company: {all_employee}')
    # for i in all_userdata:
    #     if(i.id == request.session['user_id']):
    #         print(i.id)
    #         print(i.fullname)
    #         print(i.role_id.name)
    #     print(f'This is User Data Name: {i.fullname} and the Role Nane is: {i.role_id.name}')
    
    data = {"user_data": all_userdata,
            "all_employee": all_employee,
            "all_pending_leave": all_pending_leave,
            "attendances_with_signout_time_all": attendances_with_signout_time_all,
            
            }
    return render(request,'index.html', data)

# def indexpage(request):
#     all_userdata = User.objects.all()

#     for user in all_userdata:
#         # Assuming User model has a 'role' field that is a ForeignKey to the Role model
#         role_name = user.role.name if user.role else "No Role"

#         print(f'This is User Data Name: {user.fullname} and the Role Name is: {role_name}')

#     data = {"user_data": all_userdata}
#     return render(request, 'index.html', data)