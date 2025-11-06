from django.db import models

TIPO_TRANSACAO = (
    (1, "Entrada"),
    (2, "Saída"),
)

class Categoria(models.Model):
    nome = models.CharField("Nome", max_length=25, unique=True)
    linkIcon = models.URLField("Link do Ícone")
    tipo = models.IntegerField("Tipo", choices=TIPO_TRANSACAO)

    ativo = models.BooleanField('Ativo?', default=True, editable=False)
    dataCadastro = models.DateTimeField('Data de Cadastro', auto_now_add=True)
    dataAlteracao = models.DateTimeField('Data de Alteração', auto_now=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nome