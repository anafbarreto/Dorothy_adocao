from django.contrib import admin
from banco.models import funcionarios

# Register your models here.

@admin.register(funcionarios)
class CadastroAdmmin(admin.ModelAdmin):
        list_display = ['nome', 'email', 'data']
        search_fields = ['nome', 'email']
        list_filter = ['data']