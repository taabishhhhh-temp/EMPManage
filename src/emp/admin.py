from django.contrib import admin
from .models import Employ, Profile, Client
from .forms import UserCreationForm, UserChangeForm

admin.site.register(Client)
admin.site.site_header = 'Fladdra Administration'
admin.site.site_title = 'Fladdra Administration'


class EmployAdmin(admin.ModelAdmin):
    list_display = ('fname', 'lname', 'empid', 'is_archived')
    list_filter = ('position', )
    search_fields = ('fname', 'lname')
    list_editable = ('is_archived', )

admin.site.register(Employ, EmployAdmin)


from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import MyUser


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('email', 'username', 'userType', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        # ('Personal info', {'fields': ('date_of_birth',)}),
        ('Permissions', {'fields': ('is_admin','is_staff')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'userType', 'email', 'password1', 'password2'),
        }),
    )
    search_fields = ('username', 'email', 'userType')
    ordering = ('username', 'email', 'userType')
    filter_horizontal = ()


admin.site.register(MyUser, UserAdmin)
admin.site.unregister(Group)
admin.site.register(Profile)