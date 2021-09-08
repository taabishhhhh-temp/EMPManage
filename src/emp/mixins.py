from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Employ
from django.shortcuts import get_object_or_404


class EmployeeUnarchivedQuerysetView():
    def get_queryset(self):
        return Employ.objects.unarchived()

    def get_object(self, *args, **kwargs):
        id_ = self.kwargs.get('empid')
        return get_object_or_404(Employ, empid=id_)


class StaffRequiredMixin(object):
    """
    This mixin will raise a 404 if user is neither staff nor admin
    """
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if not (request.user.userType == 'Admin' or request.user.userType == 'Staff'):
            raise Http404('You are not Authorised to view this page')
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)


class AdminRequiredMixin(object):
    """
    This Mixin will raise a 404 if the user is not Admin
    """
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if not request.user.userType == 'Admin':
            raise Http404('You are not Authorised to view this page')
        return super(AdminRequiredMixin, self).dispatch(request, *args, **kwargs)
