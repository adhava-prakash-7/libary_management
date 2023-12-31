"""
URL configuration for one project.

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
from app import views as app_view
from django.conf.urls.static import static
from django.conf.urls.static import static
from library_management import settings

urlpatterns = [
   
    path('',app_view.home,name='home'),
    path('signup',app_view.signup,name='signup'),
    path('student_login',app_view.studentlogin,name = 'userlogin'),
    path('adminlogin',app_view.adminlogin,name='adminlogin'),
    path('bookdetails',app_view.bookdetails,name='Bookdetails'),
    path('take',app_view.take,name='take'),
    path('add_book',app_view.lib,name='book'),
    path('updatebook/<pk>',app_view.updatebook,name='updatebook'),
    path('deletebook/<pk>',app_view.deletebook,name='deletebook'),
    path('takebook/<pk>',app_view.takebook,name='takebook'),
    path('retainbook/<pk>',app_view.retainbook,name='retainbook')

    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


