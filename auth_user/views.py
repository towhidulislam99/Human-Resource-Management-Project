from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import get_object_or_404
from .models import User,Role
from role.models import Role  # Import the Role model
import re
from django.contrib import messages
import os
# from django.contrib.auth.decorators import login_required

# Create your views here.

def signuppage(request):
    all_roles = Role.objects.all().order_by('pk')
    if len(all_roles) == 0:
        status = False
    else:
        status = True
    data = {"role_data": all_roles, 'status': status}
    return render(request,'register.html', data)

def signuppage_insert(request):
    if request.method == 'POST':
        role_id = request.POST.get('role_id')
        fullname = request.POST.get('fullname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')
        photo = request.FILES.get('photo')
        pattern = r"^[a-zA-Z0-9_.]+@gmail\.com$"
        
        if not all([role_id, fullname, username, email, phone, password, confirmpassword,photo]):
            messages.error(request, 'Please fill all the fields')
            return HttpResponse('Please fill all the fields')

        elif password != confirmpassword:
            messages.error(request, 'Password and Confirm Password do not match')
            return HttpResponse('Password and Confirm Password do not match')

        elif any(len(field) < 3 for field in [fullname, password, confirmpassword]):
            messages.error(request, 'Name, Password, and Confirm Password should be at least 3 characters long')
            return HttpResponse('Name, Password, and Confirm Password should be at least 3 characters long')

        elif len(phone) != 11:
            messages.error(request, 'Phone Number must be at least 11 digits long')
            return HttpResponse('Phone Number must be at least 11 digits long')

        elif not re.match(pattern, email):
            return HttpResponse('Email is not validated')
        
        else:
            try:
                role_id = int(role_id)  # Convert role_id to integer if it's a string
                role = Role.objects.get(pk=role_id)
                
                user_obj, created = User.objects.get_or_create(
                    role_id=role, fullname=fullname, username=username, email=email, phone=phone, password=password,photo = photo
                )
                
                if created:
                    messages.success(request, 'User Data created successfully')
                else:
                    messages.success(request, 'User Role Already Existed')

                return redirect('signup')

            except Role.DoesNotExist:
                messages.error(request, 'Role does not exist')
                return HttpResponse('Data Cannot be submitted')

    else:
            return HttpResponse('Page Not Found')

def signuppagedata(request):
    all_userdata = User.objects.select_related('role_id').all()
    data = {"user_data": all_userdata}
    return render(request,'authuserdata.html', data)
      
        

def signuppage_output(request):
    all_userdata = User.objects.select_related('role_id').all()
    if(len(all_userdata)==0):
        status_u = False
    else:
        status_u = True
        
    msg = messages.get_messages(request)
    data = {"user_data": all_userdata, 'status_u': status_u, 'msg': msg}
    return render(request,'authuserdata.html', data)


def edit_user(request, id):
    user_data = User.objects.select_related('role_id').get(id=id)
    all_roles = Role.objects.all()
    msg = messages.get_messages(request)
    data = {'user_data': user_data, 'msg': msg, 'all_roles': all_roles }
    messages.success(request, 'User Data created successfully')
    return render(request,'userUpdate.html', data)


# def update(request):
#     role_id = request.POST.get('role_id')
#     fullname = request.POST.get('fullname')
#     username = request.POST.get('username')
#     email = request.POST.get('email')
#     phone = request.POST.get('phone')
#     password = request.POST.get('password')

#     user_obj = get_object_or_404(User, id=role_id)
#     role_obj = get_object_or_404(Role, id=role_id)

#     # Check if new image is provided
#     if 'photo' in request.FILES:
#         # If a new image is provided, delete the old one if it exists
#         if user_obj.photo:
#             os.remove(user_obj.photo.path)
#         user_obj.photo = request.FILES['photo']

#     user_obj.role_id = role_obj
#     user_obj.fullname = fullname
#     user_obj.username = username
#     user_obj.email = email
#     user_obj.phone = phone
#     # Note: Storing passwords directly is not recommended; use Django's built-in mechanisms
#     user_obj.set_password(password)
#     user_obj.save()
    
#     return redirect('signuppage_output')

def update(request):
    id = request.POST.get('id')
    role_id = request.POST.get('role_id')
    fullname = request.POST.get('fullname')
    username = request.POST.get('username')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    password = request.POST.get('password')

    user_obj = get_object_or_404(User, id=id)
    role_obj = get_object_or_404(Role, id=role_id)
    
     # Check if new image and video files are provided
    if 'photo' in request.FILES:
        # If a new image is provided, delete the old one if it exists
        if user_obj.photo:
         os.remove(user_obj.photo.path)
        user_obj.photo = request.FILES['photo']
    
    # role_obj = Role.objects.get(id=role_id)
    # user_obj.role_id = role_obj
    user_obj.role_id = role_obj
    user_obj.fullname = fullname
    user_obj.username = username
    user_obj.email = email
    user_obj.phone = phone
    user_obj.password = password
    user_obj.save()
    return redirect('signuppage_output')

def delete_user(request, id):
    user_obj = get_object_or_404(User, id=id)
    user_obj.delete()
    return redirect('signuppage_output')


def login(request):
    if 'user_id' in request.session:
        return redirect('index')
    elif 'social_auth_google-oauth2' in request.session:
        return redirect('index')
    return render(request,'login.html')

# def login(request):
#     return render(request, 'login.html')

# def logout(request):
#     # request.session.flush()
#     # del request.session['social_auth_google-oauth2']
#     del request.session['user_id']
#     return redirect('login')


def logout(request):
    if 'user_id' in request.session:
        del request.session['user_id']
    if 'user_name' in request.session:
        del request.session['user_name']
    # if 'social_auth_google-oauth2' in request.session:
    #     del request.session['social_auth_google-oauth2']
    return redirect('login')

def login_done(request):
    uname = request.POST.get('uname')
    pw = request.POST.get('pw')

    check = User.objects.get(username=uname)
    if(check.password==pw):
        request.session['user_id'] = check.id
        request.session['user_name'] = check.username
        return redirect('index')
    return redirect('login')
