from django.db import models

class Projeto(models.Model):
    STATUS_CHOICES = [
        ('Planejamento', 'Planejamento'),
        ('Em Andamento', 'Em Andamento'),
        ('Concluído', 'Concluído'),
        ('Cancelado', 'Cancelado'),
    ]

    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    data_inicio = models.DateField()
    data_previsao_termino = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Planejamento')
    cliente_id = models.IntegerField()
    arquiteto_responsavel_id = models.IntegerField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome