from django.db import models

class Modelo(models.Model):
    nome = models.CharField(max_length=80)
    marca = models.CharField(max_length=80, null=True, blank=True)
    categoria = models.CharField(max_length=80, null=True, blank=True)
    def __str__(self):
        if self.marca == None:
            return f"{self.marca} {self.nome.upper()}"
        return f"{self.marca.upper()}, {self.nome.upper()}"