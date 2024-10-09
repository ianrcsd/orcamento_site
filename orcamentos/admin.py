from django.contrib import admin
from .models import Cliente, ProdutoServico, Orcamento, OrcamentoItem


class OrcamentoItemInline(admin.TabularInline):
    model = OrcamentoItem
    extra = 1


class OrcamentoAdmin(admin.ModelAdmin):
    inlines = [OrcamentoItemInline]


admin.site.register(Cliente)
admin.site.register(ProdutoServico)
admin.site.register(Orcamento, OrcamentoAdmin)
