from django.urls import path
from .views import employcreate, employview


app_name = 'emp'

urlpatterns = [
    path('create/', employcreate, name='create_emp'),
    path('view/', employview, name='view_emp'),
]