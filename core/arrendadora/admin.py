from django.contrib import admin

# Register your models here.

from core.arrendadora.models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class RegisterResource(resources.ModelResource):
    class Meta:
        model = Register


class RegisterAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['owner']
    list_display = ('owner', 'concepto', 'tipo',)
    resource_class = RegisterResource


admin.site.register(Owner)
admin.site.register(Status)
admin.site.register(State)
admin.site.register(Colonia)
admin.site.register(Modelo)
admin.site.register(Marca)
admin.site.register(Submarca)
admin.site.register(Tipo)
admin.site.register(Conceptos)
admin.site.register(Unidad)
admin.site.register(Register,RegisterAdmin)
