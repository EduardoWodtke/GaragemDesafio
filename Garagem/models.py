from django.db import models

class Categoria(models.Model):
    descricao = models.CharField(max_length=50)

class Marca(models.Model):
    nome = models.CharField(max_length=50)

class Modelo(models.Model):
    nome = models.CharField(max_length=50)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="Modelo", null=False, blank=False)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name="Modelo", null=True, blank=False)

class Cor(models.Model):
    nome = models.CharField(max_length=20)

class Acessorio(models.Model):
    descricao = models.CharField(max_length=50)

class Veiculo(models.Model):
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name="Veiculo", null=False)

