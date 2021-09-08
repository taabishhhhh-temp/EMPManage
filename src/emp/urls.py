from os import name
from django.urls import path
from django.urls.conf import include
# from django.views.generic.edit import CreateView
# from django.views.generic.list import ListView
# from .views import employcreate, employview, employlist, employupdate, employdelete
from .views import CreateEmp, ListEmp, ViewEmp, UpdateEmp, DeleteEmp
from rest_framework.routers import DefaultRouter


app_name = 'emp'
router = DefaultRouter()
# router.register('employ', EmployViewSet, basename='employ')


urlpatterns = [
    path('viewset/', include(router.urls)),
    path('create/', CreateEmp.as_view(), name='create_emp'),
    path('view/<int:empid>/', ViewEmp.as_view(), name='view_emp'),
    path('list/', ListEmp.as_view(), name='list_emp'),
    # path('listclass/', ListEmploy.as_view(), name='listbyclass'),
    path('update/<int:empid>/', UpdateEmp.as_view(), name='update_emp'),
    path('delete/<int:empid>/', DeleteEmp.as_view(), name='delete_emp'),
    # path('serializer/', employ_list, name="list_using_rest"), 
    # path('detail/<int:empid>/', employ_detail, name="detail_using_rest"),
    # path('listapi/', EmployAPIView.as_view(), name="list_with_class"),
    # path('single/<int:empid>/', EmployDetailsAPI.as_view(), name="single_with_class"),
    # path('genericlistapi/', GenericAPIView.as_view(), name="list_with_generic"),
    # path('genericlistapi/<int:empid>/', GenericAPIView.as_view(), name="detail_with_generic"),
    # path('genericlistapi2/', EmployListAPI.as_view(), name="list_with_class2"),
]