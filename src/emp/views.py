from django.shortcuts import render
from .forms import EmployForm
from django.contrib import messages
from .models import Employ
from django.urls import reverse

def employcreate(request, *args, **kwargs):
    form = EmployForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = EmployForm
        messages.success(request, 'Employ Created Successfully.')
        return reverse('EMP:view_emp', kwargs={'id':id})
    context = {
        'form' : form
    }
    return render(request, 'emp/create.html', context)

def employlist(request, *args, **kwargs):
    queryset = Employ.objects.all()
    context = {
        'object.list' : queryset
    }
    return render(request, 'emp/list.html', context)

def employview(request, *args, **kwargs):
    obj = Employ.objects.get(id=id)
    context = {
        'object' : obj
    }
    return render(request, 'emp/view.html', context)
