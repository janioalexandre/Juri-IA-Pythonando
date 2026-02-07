from django.contrib import admin
from .models import Cliente, Documentos

# Register your models here.

admin.site.register(Cliente)

@admin.register(Documentos)
class DocumentosAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'tipo', 'arquivo', 'data_upload')
