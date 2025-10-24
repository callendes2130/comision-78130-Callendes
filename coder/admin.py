from django.contrib import admin
from coder.models import *

#admin.site.register(T_Proceso)

@admin.register(T_Proceso)
class TProcesoAdmin (admin.ModelAdmin):
    list_display = ("identificador", "descripcion", "cargo", "fechainicio","fechafin", "totalpuestos")
    list_display_links = ("identificador", "descripcion")
    search_fields=("identificador",)
    list_filter = ("cargo","fechainicio", "fechafin")
    ordering = ("fechainicio","descripcion", "cargo")
    readonly_fields=("identificador",)