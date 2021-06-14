from os import name
from django.urls import path
# from django.views.generic.edit import CreateView
# from django.views.generic.list import ListView
# from .views import employcreate, employview, employlist, employupdate, employdelete
from .views import CreateEmp, ListEmp, ViewEmp, UpdateEmp, DeleteEmp

app_name = 'emp'

urlpatterns = [
    
    path('create/', CreateEmp.as_view(), name='create_emp'),
    path('view/<int:empid>/', ViewEmp.as_view(), name='view_emp'),
    path('list/', ListEmp.as_view(), name='list_emp'),
    # path('createclass/', CreateEmploy.as_view(), name='createempbyclass'),
    # path('listclass/', ListEmploy.as_view(), name='listbyclass'),
    path('update/<int:empid>/', UpdateEmp.as_view(), name='update_emp'),
    path('delete/<int:empid>/', DeleteEmp.as_view(), name='delete_emp')
]