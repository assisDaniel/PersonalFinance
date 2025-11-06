from django.db import models


class MetodoPagamento(models.Model):
    nome = models.CharField("Nome", max_length=25, unique=True)

    ativo = models.BooleanField('Ativo?', default=True, editable=False)
    dataCadastro = models.DateTimeField('Data de Cadastro', auto_now_add=True)
    dataAlteracao = models.DateTimeField('Data de Alteração', auto_now=True)

    class Meta:
        verbose_name = 'Método de Pagamento'
        verbose_name_plural = 'Métodos de Pagamento'

    def __str__(self):
        return self.nome