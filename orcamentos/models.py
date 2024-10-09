from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    endereco = models.TextField()

    def __str__(self):
        return self.nome


class ProdutoServico(models.Model):
    TIPO_CHOICES = [
        ("Produto", "Produto"),
        ("Serviço", "Serviço"),
    ]
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)

    def __str__(self):
        return self.nome


class Orcamento(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_criacao = models.DateTimeField(auto_now_add=True)
    titulo = models.CharField(max_length=200)
    produtos_servicos = models.ManyToManyField(ProdutoServico, through="OrcamentoItem")

    def __str__(self):
        return f"Orçamento {self.id} - {self.titulo}"


class OrcamentoItem(models.Model):
    orcamento = models.ForeignKey(Orcamento, on_delete=models.CASCADE)
    produto_servico = models.ForeignKey(ProdutoServico, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantidade} x {self.produto_servico.nome}"
