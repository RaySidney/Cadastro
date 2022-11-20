from django.contrib import admin
from .models import Pessoa, Contato

# Register your models here.
@admin.action(description='Ativar pessoas selecionadas')
def Ativar(modeladmin, request, queryset):
    queryset.update(ativa=True)

@admin.action(description='Desativar pessoas selecionadas')
def Desativar(modeladmin, request, queryset):
    queryset.update(ativa=False)




class PessoaAdmin(admin.ModelAdmin):
    list_display = [
        'nome_completo',
        'data_nascimento',
        'ativa'
    ]
    list_filter = [
        'data_nascimento',
        'ativa'
    ]
    search_fields = ['nome_completo']
    actions = [Ativar, Desativar]




admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(Contato)


