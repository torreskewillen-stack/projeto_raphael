from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'


class Produto(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=8, decimal_places=2)

    imagem = models.ImageField(
        upload_to='produtos/',
        blank=True,
        null=True
    )

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name='produtos'
    )

    estoque = models.PositiveIntegerField(default=0)
    destaque = models.BooleanField(default=False)
    ativo = models.BooleanField(default=True)

    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'


class MensagemContato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    mensagem = models.TextField()
    enviada_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.nome} - {self.email}'

    class Meta:
        verbose_name = 'Mensagem de contato'
        verbose_name_plural = 'Mensagens de contato'
        ordering = ['-enviada_em']

