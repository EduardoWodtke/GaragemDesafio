from django.db import models

class categoria(models.Model):
    descricao = models.CharField(max_length=50)
