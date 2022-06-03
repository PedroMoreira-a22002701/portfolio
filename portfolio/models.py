from django.db import models

# Create your models here.
class post(models.Model):
    autor = models.CharField(max_length=50)
    titulo = models.CharField(max_length=20)
    descricao = models.CharField(max_length=200)
    data = models.DateField()

class PontuacaoQuiz(models.Model):
    nome = models.CharField(max_length=50)
    pontos = models.IntegerField()