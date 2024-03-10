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
    path('', views.performancepage, name='performancepage'),
    path('performance_insert', views.performance_insert, name='performance_insert'),
    path('performance_list', views.performance_list, name='performance_list'),
    path('performance_view', views.performance_view, name='performance_view'),
    path('performance_edit/<int:id>/', views.performance_edit, name='performance_edit'),
    path('performance_update', views.performance_update, name='performance_update'),
    path('performance_delete/<int:id>/', views.performance_delete, name='performance_delete'),
   
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
