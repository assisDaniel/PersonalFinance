from django.contrib import admin
from unfold.admin import ModelAdmin

from transacoes.models import MetodoPagamento

@admin.register(MetodoPagamento)
class MetodoPagamentoAdmin(ModelAdmin):
    # Warn before leaving unsaved changes in changeform
    warn_unsaved_form = True  # Default: False

    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome')
    actions = ('desativarMetodoPag',)

    @admin.action(description='1 - Desativar método(s) selecionado(s)')
    def desativarMetodoPag(self, request, queryset):
        updated = queryset.update(ativo=False)
        self.message_user(request, f"{updated} método(s) desativado(s).")

    def get_actions(self, request):
        actions = super().get_actions(request) or {}
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions