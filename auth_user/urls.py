"""
URL configuration for HumanResourseManagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signuppage/', views.signuppage, name='signup'),
    path('signuppageinsert/', views.signuppage_insert, name='signuppage_insert'),
    path('signuppagedata/', views.signuppagedata, name='signuppagedata'),
    path('signuppageoutput/', views.signuppage_output, name='signuppage_output'),
    path('edit/<int:id>', views.edit_user, name='edit_user'),
    path('updateuser/', views.update, name='update_user'),  
    path('deleteuser/<int:id>', views.delete_user, name='delete_user'), 
    path("loginpage", views.login,name='login'),
    path("user/login", views.login_done,name='login_done'),
    path("user/logout", views.logout,name='logout'),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
