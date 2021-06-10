# from django.db.models.query import QuerySet, Q
from django.http.response import HttpResponseBase, HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
# from django.urls.base import reverse_lazy
from .forms import EmployForm
from django.contrib import messages
from .models import Employ
# from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
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

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data('username')
            # password = form.cleaned_data('password1')
            # user = authenticate(username=username, password=password)
            # login(request, user)
            messages.success(request, 'Account Created Successfully...')
            return HttpResponseRedirect('/accounts/login/')

    else: 
        form = UserCreationForm()
    context = {
        'form' : form
    }
    return render(request, 'registration/register.html', context)


def homePage(request):
    return render(request, 'home.html', {})

def employcreate(request, *args, **kwargs):
    form = EmployForm(request.POST or None)
    if form.is_valid():
        new_emp = form.save()
        messages.success(request, 'Employ Created Successfully...')
        return HttpResponseRedirect('/emp/list/')
    context = {
        'form' : form
    }
    return render(request, 'emp/create.html', context)


def employlist(request, *args, **kwargs):
    queryset = Employ.objects.all()
    query = request.GET.get('q', None)
    if query is not None:
        queryset = queryset.filter(empid__icontains=query)          
    context = {
        'object_list' : queryset
    }
    return render(request, 'emp/list.html', context)


def employview(request, id, *args, **kwargs):
    obj = get_object_or_404(Employ, id=id)
    context = {
        'object' : obj
    }
    return render(request, 'emp/view.html', context)


def employupdate(request, id):
    obj = get_object_or_404(Employ, id=id)
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


def employdelete(request, id=None):
    obj = get_object_or_404(Employ, id=id)
    context = {
        'object': obj,
    }
    if request.method == 'POST':
        obj.delete()
        messages.success(request, 'Employ Details Deleted...')
        return HttpResponseRedirect('/emp/list/')
    return render(request, 'emp/delete.html', context)
