from django.contrib import admin

from models import Servidor

class ServidorAdmin(admin.ModelAdmin):
    
    models = Servidor
    
    list_display = ['nome', 'user']
    search_fields = ['nome']
admin.site.register(Servidor, ServidorAdmin)
