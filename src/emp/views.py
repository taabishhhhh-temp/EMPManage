from django.db.models.query import Q
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework import status
from rest_framework.response import Response
from .forms import EmployForm, RegistrationForm
from .models import Employ
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from .mixins import StaffRequiredMixin, AdminRequiredMixin, EmployeeUnarchivedQuerysetView

def registerUser(request):
    if request.user.is_authenticated:
        messages.info(request, 'You are logged in')
        return redirect('homepage')

    form = RegistrationForm(request.POST or None)        
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/home')
     
        context = {
            'form' : form
        }
    return render(request, 'registration/register.html', context)

def user_login(request):
    if request.user.is_authenticated:
        messages.info(request, 'You are already logged in')
        return redirect('/')

    if request.method == 'POST':
        username = request.POST['username']  
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login_view')
            
    return render(request, 'login.html', {})


@login_required(login_url='login/')
def logout(request):
    logout(request)
    return HttpResponseRedirect('home/')

def homePage(request):
    return render(request, 'home.html', {})


class CreateEmp(LoginRequiredMixin, AdminRequiredMixin, CreateView):
    form_class = EmployForm
    template_name = 'emp/create.html'
    queryset = Employ.objects.all()
    success_message = 'Employee Created Successfully...'
    '''
    after success it will go to the get_absolute_url, success_url can also be provided
    '''
    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)


class ListEmp(LoginRequiredMixin, StaffRequiredMixin, ListView):
    template_name = 'emp/list.html'
    # myqueryset = Employ.objects.unarchived()
    model = Employ
    def get_queryset(self):
        query = self.request.GET.get('q', None)
        myqueryset = self.model.objects.unarchived()
        if query is not None:
            myqueryset = myqueryset.filter(
                                    Q(empid__icontains=query) |
                                    Q(employID__icontains=query) |
                                    Q(fname__icontains=query) |
                                    Q(lname__icontains=query) |
                                    Q(personalEmail__icontains=query) |
                                    Q(fladdraEmail__icontains=query) |
                                    Q(mobile__icontains=query) |
                                    Q(position__icontains=query) |
                                    Q(github__icontains=query) |
                                    Q(education__icontains=query) |
                                    Q(address__icontains=query)
            )
        return myqueryset

class ViewEmp(EmployeeUnarchivedQuerysetView, LoginRequiredMixin, StaffRequiredMixin, DetailView):
    template_name = 'emp/view.html'
    slug_field = 'empid'
    slug_url_kwarg = 'empid'

    '''
    get_queryset and get_object are defined in the EmployeeUnarchivedQuerysetView mixin
    '''

class UpdateEmp(EmployeeUnarchivedQuerysetView, LoginRequiredMixin, AdminRequiredMixin, UpdateView):
    form_class = EmployForm
    template_name = 'emp/update.html'
    success_message = 'Details Updated Successfully...'
    slug_field = 'empid'
    slug_url_kwarg = 'empid'
    '''
    get_queryset and get_object are defined in the EmployeeUnarchivedQuerysetView mixin
    '''
    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)


class DeleteEmp(EmployeeUnarchivedQuerysetView, LoginRequiredMixin, AdminRequiredMixin, DeleteView):
    template_name = 'emp/delete.html'
    success_message = 'Details Deleted Succesfully...'
    queryset = Employ.objects.unarchived()
    slug_field = 'empid'
    slug_url_kwarg = 'empid'
    '''
    get_queryset and get_object are defined in the EmployeeUnarchivedQuerysetView mixin
    '''
    '''
    overridding the default delete method to archive the objects instead of deleting
    '''
    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.is_archived = True
        obj.save()
        messages.success(self.request, self.success_message)
        return HttpResponseRedirect('/emp/list')



# from django.http import JsonResponse
# from rest_framework.parsers import JSONParser
# from django.views.decorators import csrf
# from django.views.decorators.csrf import csrf_exempt
# from .serializer import EmploySerializer


# @csrf_exempt
# def employ_list(request):

#     if request.method == 'GET':
#         employs = Employ.objects.all()
#         serializer = EmploySerializer(employs, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = EmploySerializer(data=data)

#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)


# @csrf_exempt
# def employ_detail(request, empid):
#     try:
#         employ = Employ.objects.get(empid=empid)
#     except Employ.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'GET':
#         serializer = EmploySerializer(employ)
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = EmploySerializer(employ,data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         employ.delete()
#         return HttpResponse(status=204)

# from rest_framework.decorators import api_view
# from rest_framework.response import Response

# @api_view(['GET', 'POST',])
# def employ_list(request):

#     if request.method == 'GET':
#         employs = Employ.objects.all()
#         serializer = EmploySerializer(employs, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = EmploySerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# # @csrf_exempt

# @api_view(['GET', 'PUT', 'DELETE',],)
# def employ_detail(request, empid):
#     try:
#         employ = Employ.objects.get(empid=empid)
#     except Employ.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = EmploySerializer(employ)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = EmploySerializer(employ,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         employ.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# from rest_framework.views import APIView

# class EmployAPIView(APIView):
#     def get(self, request):
#         employs = Employ.objects.all()
#         serializer = EmploySerializer(employs, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = EmploySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class EmployDetailsAPI(APIView):

#     def get_object(self, empid):
#         try:
#             return Employ.objects.get(empid=empid)
#         except Employ.DoesNotExist:
#             return HttpResponse(status=status.HTTP_404_NOT_FOUND)

#     def get(self, request, empid):
#         employ = self.get_object(empid)
#         serializer = EmploySerializer(employ)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def put(self, request, empid):
#         employ = self.get_object(empid)
#         serializer = EmploySerializer(employ, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, empid):
#         employ = self.get_object(empid)
#         employ.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class EmployListAPI(APIView):
#     def get(self, request):
#         employs = Employ.objects.all()
#         serializer = EmploySerializer(employs, many=True)
#         return Response(data=serializer.data, status=status.HTTP_200_OK)

#     def post(self, request):
#         serializer = EmploySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=request.data, status=status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)

        
        
# from rest_framework import generics
# from rest_framework import mixins
# from rest_framework.authentication import SessionAuthentication, TokenAuthentication, BasicAuthentication
# from rest_framework.permissions import IsAuthenticated

# class GenericAPIView(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
#     serializer_class = EmploySerializer
#     queryset = Employ.objects.all()
#     authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication, ]
#     permission_classes = [IsAuthenticated, ]
#     lookup_field = 'empid'
#     '''
#     Made 2 separate urls, 1 with empid and without the empid so that all operations can be performed on the same url
#     '''
#     def get(self, request, empid=None):
#         if empid is not None:
#             return self.retrieve(request, empid)
#         else:
#             return self.list(request)
            
#     def post(self, request):
#         return self.create(request)

#     def put(self, request, empid):
#         return self.update(request, empid)

#     def delete(self, request, empid):
#         return self.destroy(request, empid)

    
# from rest_framework import viewsets

# class EmployViewSet(viewsets.ViewSet):
    
#     def list(self, request):
#         employs = Employ.objects.all()
#         serializer = EmploySerializer(employs, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def create(self, request):
#         serializer = EmploySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def retrieve(self, request, pk=None):
#         queryset = Employ.objects.all()
#         obj = get_object_or_404(Employ, empid=pk)
#         serializer = EmploySerializer(obj)
#         return Response(serializer.data, status=status.HTTP_200_OK)

