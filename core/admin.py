from django.contrib import admin
from .models import Categoria, Produto, MensagemContato


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_fields = ('nome',)


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nome',
        'preco',
        'categoria',
        'estoque',
        'destaque',
        'ativo'
    )

    list_filter = ('categoria', 'destaque', 'ativo')
    search_fields = ('nome', 'descricao')


@admin.register(MensagemContato)
class MensagemContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'enviada_em')
    search_fields = ('nome', 'email')
    readonly_fields = ('enviada_em',)

