from django.urls.base import reverse, reverse_lazy
# from django.contrib import messages
# from django.urls import reverse
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import authenticate, login
from django.db.models.query import Q, QuerySet
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import  render, get_object_or_404
from .forms import EmployForm
from .models import Employ
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth import logout

@login_required(login_url='login/')
def logout(request):
    logout(request)
    return HttpResponseRedirect('home/')

def homePage(request):
    return render(request, 'home.html', {})


class MyGetQuerySet():
    model = Employ
    def get_queryset(self, request, *args, **kwargs):
        QuerySet =  self.model.objects.filter(is_archived=False)
        return QuerySet
    

class CreateEmp(LoginRequiredMixin, CreateView):
    form_class = EmployForm
    template_name = 'emp/create.html'
    queryset = Employ.objects.all()
    success_message = 'Employee Created Successfully...'

    #after success it will go to the get_absolute_url
    #success_url can also be provided

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)


class ListEmp(LoginRequiredMixin, ListView):
    template_name = 'emp/list.html'
    # queryset = Employ.objects.filter(is_archived=False)
    model = Employ

    def get_queryset(self):
        # messages.success(self.request, 'test message.')
        queryset = self.model.objects.filter(is_archived=False)
        query = self.request.GET.get('q', None)
        # query = str(query.title())
        if query is not None:
            queryset = self.model.objects.filter(
                                    Q(is_archived=False) &
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
        return queryset


class ViewEmp(LoginRequiredMixin, MyGetQuerySet, DetailView):
    template_name = 'emp/view.html'
    # queryset = Employ.objects.filter(is_archived=False)
    # model = Employ
    
    # queryset = get_queryset()

    def get_object(self):
        id_ = self.kwargs.get('empid')
        return get_object_or_404(Employ, empid=id_)


class UpdateEmp(LoginRequiredMixin, UpdateView):
    form_class = EmployForm
    template_name = 'emp/update.html'
    queryset = Employ.objects.filter(is_archived=False)
    success_message = 'Details Updated Successfully...'

    #after success it will go to the get_absolute_url
    #success_url can also be provided

    def get_queryset(self):
        return self.model.objects.filter(is_archived=False)

    def get_object(self):
        id_ = self.kwargs.get('empid')
        return get_object_or_404(Employ, empid=id_)
        
    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)


class DeleteEmp(LoginRequiredMixin, DeleteView, MyGetQuerySet):
    template_name = 'emp/delete.html'
    success_message = 'Details Deleted Succesfully...'
    # queryset = Employ.objects.filter(is_archived=False)
    # success_url = '/emp/list'
    #here success_url is required because it cant use to the get_absolute_url since the object is deleted

    # def get_queryset(self):
    #     return self.model.objects.filter(is_archived=False)

    def get_object(self):
        id_ = self.kwargs.get('empid')
        return get_object_or_404(Employ, empid=id_)

    def delete(self, request, *args, **kwargs): 
        #overridding the default delete method to archive the objects instead of deleting
        # super().delete(request, *args, **kwargs)
        obj = self.get_object()
        obj.is_archived = True
        obj.save()
        messages.success(self.request, self.success_message)
        return HttpResponseRedirect('/emp/list')
        


# # def register(request):
# #     if request.method == 'POST':
# #         form = UserCreationForm(request.POST)
# #         if form.is_valid():
# #             form.save()
# #             # username = form.cleaned_data('username')
# #             # password = form.cleaned_data('password1')
# #             # user = authenticate(username=username, password=password)
# #             # login(request, user)
# #             messages.success(request, 'Account Created Successfully...')
# #             return HttpResponseRedirect('/login/')
# #
# #     else: 
# #         form = UserCreationForm()
# #     context = {
# #         'form' : form
# #     }
# #     return render(request, 'registration/register.html', context)


# @login_required
# def employcreate(request, *args, **kwargs):
#     # fname = request.POST.get('fname')
#     # lname = request.POST.get('lname')
#     # email = request.POST.get('email')
#     # mobile = request.POST.get('mobile')
#     # position = request.POST.get('position')
#     # print(lname,fname,email,mobile,position)
#     # Employ.objects.create(fname=fname, lname=lname, email=email, mobile=mobile, position=position)
#     form = EmployForm(request.POST or None)
#     if form.is_valid():
#         new_emp = form.save()
#         messages.success(request, 'Employ Created Successfully...')
#         return HttpResponseRedirect('/emp/list/')
#     context = {
#         'form' : form
#     }
#     return render(request, 'emp/create.html', context)


# # @login_required(login_url='/login/')
# def employlist(request, *args, **kwargs):
#     queryset = Employ.objects.all()
#     query = request.GET.get('q', None)
#     # query = str(query.title())
#     if query is not None:
#         queryset = queryset.filter(
#                                 Q(empid__icontains=query) |
#                                 Q(EmployID__icontains=query) |
#                                 Q(fname__icontains=query) |
#                                 Q(lname__icontains=query) |
#                                 Q(personalEmail__icontains=query) |
#                                 Q(fladdraEmail__icontains=query) |
#                                 Q(mobile__icontains=query) |
#                                 Q(position__icontains=query) |
#                                 Q(github__icontains=query) |
#                                 Q(education__icontains=query) |
#                                 Q(address__icontains=query)                                
#                                     )
#     context = {
#         'object_list' : queryset,
#         'length' : len(queryset)
#     }
#     return render(request, 'emp/list.html', context)


# # @login_required(login_url='/login/')
# def employview(request, empid, *args, **kwargs):
#     obj = get_object_or_404(Employ, empid=empid)
#     context = {
#         'object' : obj
#     }
#     return render(request, 'emp/view.html', context)


# # @login_required(login_url='/login/')
# def employupdate(request, empid):
#     print(
#         'employee update callled : ', request.POST
#     )
#     obj = get_object_or_404(Employ, empid=empid)
#     form = EmployForm(request.POST or None, instance=obj)
#     context = {
#         'form':form,
#         'object': obj
#     }
#     if form.is_valid():
#         print('form is valid')
#         form.save()
#         messages.success(request, 'Employ Details Updated Successfully...')
#         # return HttpResponseRedirect('https://www.google.co.in/')
#         return HttpResponseRedirect('/emp/list/')
#         # return reverse('emp:view', kwargs={'object' : obj })
#     else:
#         print('form not valid')
#     return render(request, 'emp/update.html', context)


# # @login_required(login_url='/login/')
# def employdelete(request, empid=None):
#     obj = get_object_or_404(Employ, empid=empid)
#     context = {
#         'object': obj,
#     }
#     if request.method == 'POST':
#         obj.delete()
#         messages.success(request, 'Employ Details Deleted...')
#         return HttpResponseRedirect('/emp/list/')
#     return render(request, 'emp/delete.html', context)
