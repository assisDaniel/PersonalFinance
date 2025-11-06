from django.db import models
from djmoney.money import Money
from djmoney.models.fields import MoneyField
from djmoney.models.validators import MinMoneyValidator

from transacoes.models import Categoria, MetodoPagamento

TIPO_TRANSACAO = (
    (1, "Entrada"),
    (2, "Saída"),
)

class Transacao(models.Model):
    tipo = models.IntegerField("Tipo", choices=TIPO_TRANSACAO)
    quantia = MoneyField(
        "Quantia",
        max_digits=20,
        decimal_places=2,
        default_currency='BRL',
        validators=[
            MinMoneyValidator(Money(0, "BRL")),
        ]
    )
    dataTransacao = models.DateField("Data")
    categoria = models.ForeignKey(Categoria, verbose_name="Categoria", on_delete=models.PROTECT)
    metodoPagamento = models.ForeignKey(MetodoPagamento, verbose_name="Método de Pagamento", on_delete=models.PROTECT)
    descricao = models.TextField("Descrição", max_length=75)

    ativo = models.BooleanField('Ativo?', default=True, editable=False)
    dataCadastro = models.DateTimeField('Data de Cadastro', auto_now_add=True)
    dataAlteracao = models.DateTimeField('Data de Alteração', auto_now=True)

    class Meta:
        verbose_name = 'Transação'
        verbose_name_plural = 'Transações'

    def __str__(self):
        return f"{self.tipo} - {self.quantia}"