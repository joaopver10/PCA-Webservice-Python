from django.contrib import admin
from .models import Estados


class EstadosAdmin(admin.ModelAdmin):
    list_display = ('sigla','descricao' )


admin.site.register(Estados, EstadosAdmin)