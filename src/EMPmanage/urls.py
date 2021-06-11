"""EMPmanage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django import urls
import django
from django.contrib import admin
from django.urls import path, include
from emp.views import homePage
from django.contrib.auth.views import LoginView, logout_then_login

urlpatterns = [
    # path('accounts/', include('django.contrib.auth.urls')),
    path('', homePage, name='homepage'),
    path('login/', LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', logout_then_login, name='logout'),  #this will redirect to login page after logout 
    path('home/', homePage, name='homepage'),
    # path('register/', register, name='register'), # {template_name:'register/register.html'}
    path('emp/', include('emp.urls')),
    path('admin/', admin.site.urls),
]
