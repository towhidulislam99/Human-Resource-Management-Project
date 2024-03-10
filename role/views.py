from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Role
from django.contrib import messages
from auth_user.models import User

def rolepage(request):
    all_userdata = User.objects.select_related('role_id').all()
    data = {"user_data": all_userdata}
    return render(request,'role.html', data)

def role_insert(request):
    role = request.POST.get('role')

    if not role:
        messages.error(request, 'The field cannot be empty')
    else:
        role_obj, created = Role.objects.get_or_create(name=role)

        if created:
            messages.success(request, 'User Role created successfully')
        else:
            messages.success(request, 'User Role Already Existed')

    return redirect('roleoutput')


def roleoutput(request):
    all_userdata = User.objects.select_related('role_id').all()
    all_data = Role.objects.all()
    if(len(all_data)==0):
        status = False
    else:
        status = True
        
    msg = messages.get_messages(request)
    data = {"role_data": all_data,"user_data": all_userdata, 'status': status, 'msg': msg}
    return render(request,'role.html', data)


def role_edit(request, id):
    all_userdata = User.objects.select_related('role_id').all()
    all_data = Role.objects.get(id=id)
    data = {"role_data": all_data,"user_data": all_userdata}
    return render(request,'roleupdate.html', data)

def update(request):
    id = request.POST.get('id')
    name = request.POST.get('role')
    
    role_obj = get_object_or_404(Role, id=id)
    role_obj.name = name
    role_obj.save()
    return redirect('roleoutput')

def delete_role(request, id):
    role_obj = get_object_or_404(Role, id=id)
    role_obj.delete()
    return redirect('roleoutput')
