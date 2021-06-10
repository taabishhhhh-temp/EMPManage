from django.contrib import admin
from .models import Employ


admin.site.site_header = 'Fladdra Administration'
admin.site.site_title = 'Fladdra Administration'


class EmployAdmin(admin.ModelAdmin):

    list_display = ('fname', 'lname', 'empid', 'position')
    list_filter = ('position', )
    search_fields = ('fname', 'lname')
    list_editable = ('position', )



admin.site.register(Employ, EmployAdmin)

