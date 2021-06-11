from os import name
from django.urls import path
from .views import employcreate, employview, employlist, employupdate, employdelete
# from .views import CreateEmploy, ListEmploy 

app_name = 'emp'

urlpatterns = [
    
    path('create/', employcreate, name='create_emp'),
    path('view/<slug:empid>/', employview, name='view_emp'),
    path('list/', employlist, name='list_emp'),
    # path('createclass/', CreateEmploy.as_view(), name='createempbyclass'),
    # path('listclass/', ListEmploy.as_view(), name='listbyclass'),
    path('update/<slug:empid>/', employupdate, name='update_emp'),
    path('delete/<slug:empid>/', employdelete, name='delete_emp')
]