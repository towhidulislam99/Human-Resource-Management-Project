from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Designation
from django.contrib import messages
from auth_user.models import User

def designationpage(request):
        all_userdata = User.objects.select_related('role_id').all()
        data = {"user_data": all_userdata}
        
        return render(request,'designation.html', data)

def designation_insert(request):
    designation = request.POST.get('designation')

    if not designation:
        messages.error(request, 'The field cannot be empty')
    else:
        designation_obj, created = Designation.objects.get_or_create(name=designation)

        if created:
            messages.success(request, 'User Role created successfully')
        else:
            messages.success(request, 'User Role Already Existed')

    return redirect('designationoutput')


def designationoutput(request):
    all_data = Designation.objects.all()
    all_userdata = User.objects.select_related('role_id').all()
    if(len(all_data)==0):
        status = False
    else:
        status = True
        
    msg = messages.get_messages(request)
    data = {"designation_data": all_data,"user_data": all_userdata, 'status': status, 'msg': msg}
    return render(request,'designation.html', data)


def designation_edit(request, id):
    all_data = Designation.objects.get(id=id)
    all_userdata = User.objects.select_related('role_id').all()
    data = {"designation_data": all_data, "user_data": all_userdata }
    return render(request,'designationupdate.html', data)

def updatedesignation(request):
    id = request.POST.get('id')
    name = request.POST.get('designation')
    
    designation_obj = get_object_or_404(Designation, id=id)
    designation_obj.name = name
    designation_obj.save()
    return redirect('designationoutput')

def delete_designation(request, id):
    designation_obj = get_object_or_404(Designation, id=id)
    designation_obj.delete()
    return redirect('designationoutput')
