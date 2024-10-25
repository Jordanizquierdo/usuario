from django.contrib import admin
from .models import User
from .forms import FormUser

class UserAdmin(admin.ModelAdmin):
    form = FormUser
    list_display = ['id','nombre', 'apellido', 'numero', 'correo', 'direccion', 'rut']
    search_fields = ['id','nombre', 'apellido', 'numero', 'correo', 'direccion', 'rut']
    list_editable = ['nombre', 'apellido', 'numero', 'correo', 'direccion', 'rut'] 
    actions = ['delete_selected'] 

    def has_delete_permission(self, request, obj=None):
        return True 

    def has_change_permission(self, request, obj=None):
        return True

admin.site.register(User, UserAdmin)
