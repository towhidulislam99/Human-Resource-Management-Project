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
    # path('admin/', admin.site.urls),
    path('', views.diciplinarypage, name='diciplinarypage'),
    path('diciplinaryinsert/', views.diciplinary_insert, name='diciplinary_insert'),
    path('diciplinaryoutput/', views.diciplinaryoutput, name='diciplinaryoutput'),
    path('diciplinaryedit/<int:id>', views.diciplinary_edit, name='diciplinary_edit'),
    path('diciplinaryupdate/', views.diciplinary_update, name='diciplinary_update'),
    path('diciplinarydelete/<int:id>', views.diciplinary_delete, name='diciplinary_delete'),
    
     # path('employeeview/<int:id>', views.employeeview, name='employee_view'),
    # path('employeelist/', views.employeelist, name='employee_list'),
    
    
    # path('designationedit/<int:id>', views.designation_edit, name='edit_designation'),
    # path('updatedesignation', views.updatedesignation, name='designation_update'),
    # path('designationoutput/<int:id>', views.delete_designation, name='delete_designation'),
    
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
