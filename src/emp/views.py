from django.db.models.query import QuerySet, Q
from django.http.response import HttpResponseBase, HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
# from django.urls.base import reverse_lazy
from .forms import EmployForm
from django.contrib import messages
from .models import Employ
# from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView


# class CreateEmploy(CreateView):
#     template_name = 'emp/create.html'
#     form_class_ = EmployForm
#     queryset = Employ.objects.all()

#     def form_valid(self, form):
#         return super().form_valid(form)

# class ListEmploy(ListView):
#     template_name = 'emp/list.html'
#     queryset = Employ.objects.all()

# from django.contrib.auth import logout
# def logout(request):
#     logout(request)
#     return HttpResponseRedirect('home/')


# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # username = form.cleaned_data('username')
#             # password = form.cleaned_data('password1')
#             # user = authenticate(username=username, password=password)
#             # login(request, user)
#             messages.success(request, 'Account Created Successfully...')
#             return HttpResponseRedirect('/login/')
#
#     else: 
#         form = UserCreationForm()
#     context = {
#         'form' : form
#     }
#     return render(request, 'registration/register.html', context)


def homePage(request):
    return render(request, 'home.html', {})

@login_required
def employcreate(request, *args, **kwargs):
    fname = request.POST.get('fname')
    lname = request.POST.get('lname')
    email = request.POST.get('email')
    mobile = request.POST.get('mobile')
    position = request.POST.get('position')
    # print(lname,fname,email,mobile,position)
    Employ.objects.create(fname=fname, lname=lname, email=email, mobile=mobile, position=position)
    # form = EmployForm(request.POST or None)
    # if form.is_valid():
    #     new_emp = form.save()
    #     messages.success(request, 'Employ Created Successfully...')
    #     return HttpResponseRedirect('/emp/list/')
    # context = {
    #     'form' : form
    # }
    return render(request, 'emp/create.html', {})


# @login_required(login_url='/login/')
def employlist(request, *args, **kwargs):
    queryset = Employ.objects.all()
    query = request.GET.get('q', None)
    # query = str(query.title())
    if query is not None:
        queryset = queryset.filter(
                                Q(empid__icontains=query) |
                                Q(fname__icontains=query) |
                                Q(lname__icontains=query) |
                                Q(email__icontains=query) |
                                Q(mobile__icontains=query)|
                                Q(position__icontains=query)                                     
                                    )
    context = {
        'object_list' : queryset
    }
    return render(request, 'emp/list.html', context)


# @login_required(login_url='/login/')
def employview(request, empid, *args, **kwargs):
    obj = get_object_or_404(Employ, empid=empid)
    context = {
        'object' : obj
    }
    return render(request, 'emp/view.html', context)


# @login_required(login_url='/login/')
def employupdate(request, empid):
    obj = get_object_or_404(Employ, empid=empid)
    form = EmployForm(request.POST or None, instance=obj)
    context = {
        'form':form,
        'object': obj
    }
    if form.is_valid():
        form.save()
        messages.success(request, 'Employ Details Updated Successfully...')
        # return HttpResponseRedirect('https://www.google.co.in/')
        return HttpResponseRedirect('/emp/list/')
        # return reverse('emp:view', kwargs={'object' : obj })
    return render(request, 'emp/update.html', context)


# @login_required(login_url='/login/')
def employdelete(request, empid=None):
    obj = get_object_or_404(Employ, empid=empid)
    context = {
        'object': obj,
    }
    if request.method == 'POST':
        obj.delete()
        messages.success(request, 'Employ Details Deleted...')
        return HttpResponseRedirect('/emp/list/')
    return render(request, 'emp/delete.html', context)
