from django.db import models

class Project(models.Model):
    STATUS_CHOICES = (
        ('Em Andamento', 'Em Andamento'),
        ('Concluído', 'Concluído'),
        ('Pendente', 'Pendente'),
    )

    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pendente')
    cliente = models.CharField(max_length=255) # Placeholder as requested
    data_inicio = models.DateField()
    data_fim_prevista = models.DateField()

    def __str__(self):
        return self.nome