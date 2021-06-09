from django.db.models.query import QuerySet
from django.http.response import HttpResponseBase, HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
# from django.urls.base import reverse_lazy
from .forms import EmployForm
from django.contrib import messages
from .models import Employ
from django.urls import reverse
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


def employcreate(request, *args, **kwargs):
    form = EmployForm(request.POST or None)
    if form.is_valid():
        new_emp = form.save()
        messages.success(request, 'Employ Created Successfully...')
        return redirect(new_emp.get_absolute_url())
    context = {
        'form' : form
    }
    return render(request, 'emp/create.html', context)


def employlist(request, *args, **kwargs):
    queryset = Employ.objects.all()
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
    # id_ = Employ.objects.get()
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
        return HttpResponseRedirect('/emp/view/{id}/'.format(id=obj.id))
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
