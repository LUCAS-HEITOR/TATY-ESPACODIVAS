from django.contrib import admin
from .models import Servico, Contato, Reserva, Trabalho

# Register your models here.

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'preco', 'destaque', 'ordem']
    list_editable = ['destaque', 'ordem']
    list_filter = ['destaque']
    search_fields = ['nome', 'descricao']


@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'telefone', 'data_envio']
    list_filter = ['data_envio']
    search_fields = ['nome', 'email', 'telefone']
    readonly_fields = ['data_envio']


@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'servico', 'data_desejada', 'horario', 'telefone', 'data_criacao']
    list_filter = ['data_desejada', 'servico', 'data_criacao']
    search_fields = ['nome', 'telefone', 'email']
    readonly_fields = ['data_criacao']


@admin.register(Trabalho)
class TrabalhoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'servico', 'destaque', 'ordem', 'data_criacao']
    list_editable = ['destaque', 'ordem']
    list_filter = ['destaque', 'servico', 'data_criacao']
    search_fields = ['titulo', 'descricao']
    readonly_fields = ['data_criacao']
