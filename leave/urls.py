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
from .views import change_leave_status

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('index/', views.leaveindex, name='leaveindex'),
    path('', views.leavepage, name='leavepage'),
    path('leave_list/', views.leave_list, name='leave_list'),
    path('leave_edit/<int:id>', views.leave_edit, name='leave_edit'),
    path('leave_update/', views.leave_update, name='leave_update'),
    path('leave_delete/<int:id>', views.leave_delete, name='leave_delete'),
    path('leaveview/<int:id>', views.leave_view, name='leave_view'),
    path('leave/<int:leave_id>/approve/', change_leave_status, {'new_status': 'Approved'}, name='approve_leave'),
    path('leave/<int:leave_id>/reject/', change_leave_status, {'new_status': 'Rejected'}, name='reject_leave'),
    path('appoved_user/', views.appoved_user, name='appoved_user'),
    path('reject_user/', views.reject_user, name='reject_user'),
    
    # path('leave_approval/', views.leave_approval, name='leave_approval'),
   
    
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
