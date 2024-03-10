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
from django.urls import path,include
from . import views

urlpatterns = [
    path('dj-admin/', admin.site.urls),
    path('index/', views.indexpage, name='index'),
    path('admin/', include('auth_user.urls')),
    path('admin/', include('role.urls')),
    path('admin/', include('department.urls')),
    path('admin/', include('designation.urls')),
    path('user/', include('employee.urls')),
    path('diciplinary/', include('diciplinary.urls')),
    path('attendance/', include('attendance.urls')),
    path('leave/', include('leave.urls')),
    path('performance/', include('performance.urls')),
   
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
