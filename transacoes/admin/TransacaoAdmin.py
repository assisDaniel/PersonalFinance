from django.contrib import admin
from unfold.admin import ModelAdmin
from django.utils.html import format_html

from transacoes.models import Transacao

@admin.register(Transacao)
class TransacaoAdmin(ModelAdmin):
    # Warn before leaving unsaved changes in changeform
    warn_unsaved_form = True  # Default: False

    list_display = ('id', 'tipo_colored', 'categoria', 'quantia', 'metodoPagamento', 'ativo')
    list_display_links = ('id', 'tipo_colored')
    ordering = ('id', 'tipo')
    actions = ['desativarTransacao']

    def tipo_colored(self, obj):
        try:
            isEntrada = int(obj.tipo) == 1
        except Exception:
            isEntrada = False

        color = '#00FF7F' if isEntrada else '#FF4C4C'
        label = obj.get_tipo_display() if hasattr(obj, 'get_tipo_display') else str(obj.tipo)

        return format_html('<span style="color:{}">{}</span>', color, label)
    tipo_colored.short_description = 'Tipo'

    @admin.action(description='1 - Desativar transação(ões) selecionada(s)')
    def desativarTransacao(self, request, queryset):
        updated = queryset.update(ativo=False)
        self.message_user(request, f"{updated} transação(ões) desativada(s).")

    def get_actions(self, request):
        actions = super().get_actions(request) or {}
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions
