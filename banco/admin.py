from django.contrib import admin
from .models import cadastro_animais, Adotante, adocao, funcionarios
from .forms import FuncionarioForm

# Register your models here.

@admin.register(cadastro_animais)
class CadastroAnimaisAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'idade', 'especie', 'raca', 'porte', 'sexo', 'castrado', 'vacinado', 'adotado', 'data']
    list_filter = ['especie', 'castrado', 'vacinado', 'adotado']
    search_fields = ['nome', 'raca']
    ordering = ['-data']

@admin.register(Adotante)
class AdotanteAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'cpf', 'idade', 'telefone', 'email', 'termo_responsabilidade']
    list_filter = ['termo_responsabilidade']
    search_fields = ['nome', 'cpf', 'email']
    ordering = ['nome']

@admin.register(adocao)
class AdocaoAdmin(admin.ModelAdmin):
    list_display = ['id', 'animais', 'adotante', 'termo_aceito', 'data']
    list_filter = ['termo_aceito']
    search_fields = ['animais__nome', 'adotante__nome']
    ordering = ['-data']

class FuncionarioAdmin(admin.ModelAdmin):
    form = FuncionarioForm
    list_display = ['id', 'nome', 'email', 'cargo', 'usuario']
    list_filter = ['cargo']
    search_fields = ['nome', 'email', 'usuario']
    ordering = ['nome']

admin.site.register(funcionarios, FuncionarioAdmin)
