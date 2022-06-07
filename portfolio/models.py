from django.db import models

# Create your models here.
class post(models.Model):
    autor = models.CharField(max_length=50)
    titulo = models.CharField(max_length=20)
    descricao = models.CharField(max_length=200)
    data = models.DateField(auto_now_add=True)

class PontuacaoQuiz(models.Model):
    nome = models.CharField(max_length=50)
    pontos = models.IntegerField()

class cadeira(models.Model):
    nome = models.CharField(max_length=50)
    ano = models.CharField(max_length=6)
    semestre = models.CharField(max_length=20)
    anoLetivo = models.CharField(max_length=12)
    descricao = models.CharField(max_length=500)
    ects = models.IntegerField(default=0)
    projecto = models.CharField(max_length=50)
    review = models.CharField(max_length=10)

class projecto(models.Model):
    nome = models.CharField(max_length=50)
    imagem = models.ImageField(upload_to="pictures/")
    descricao = models.CharField(max_length=500)
    github = models.URLField(blank=True)

class Picture(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pictures/', blank=True)