from django.contrib import admin
from .models import Habilidades, Empleado


# Register your models here.
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'departamento',
        'job',
        'full_name',
        'id',
    )

    def full_name(self, obj):
        return obj.first_name + ' ' + obj.last_name

    search_fields = ('first_name',)
    list_filter = ('departamento', 'job', 'Habilidades',)
    filter_horizontal = ('Habilidades',)


admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Habilidades)