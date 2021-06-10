from os import name
from django.urls import path
from .views import employcreate, employview, employlist, employupdate, employdelete, register
# from .views import CreateEmploy, ListEmploy 

app_name = 'emp'

urlpatterns = [
    
    path('create/', employcreate, name='create_emp'),
    path('view/<int:id>/', employview, name='view_emp'),
    path('list/', employlist, name='list_emp'),
    # path('createclass/', CreateEmploy.as_view(), name='createempbyclass'),
    # path('listclass/', ListEmploy.as_view(), name='listbyclass'),
    path('update/<int:id>/', employupdate, name='update_emp'),
    path('delete/<int:id>/', employdelete, name='delete_emp')
]