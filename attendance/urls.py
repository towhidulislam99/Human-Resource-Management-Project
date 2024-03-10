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
    path('', views.attendancepage, name='attendancepage'),
    path('attendance_insert', views.attendance_insert, name='attendance_insert'),
    path('attendance_view', views.attendance_view, name='attendance_view'),
    path('attendance_list', views.attendance_list, name='attendance_list'),
    path('attendance_edit/<int:id>/', views.attendance_edit, name='attendance_edit'),
    path('attendance_update', views.attendance_update, name='attendance_update'),
    path('attendance_delete/<int:id>/', views.attendance_delete, name='attendance_delete'),
    path('signout/<int:attendance_id>/', views.signout_view, name='signout'),
    path('attendance_present', views.attendance_present, name='attendance_present'),
    path('attendance_absent', views.attendance_absent, name='attendance_absent'),
   
    
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
