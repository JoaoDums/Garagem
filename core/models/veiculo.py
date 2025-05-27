from django.db import models
from core.models import Modelo, Cor, Acessorio

class Veiculo(models.Model):
    ano = models.IntegerField(default=0, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2, )
    modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT, related_name="veiculos")
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name="veiculos")
    acessorio = models.ManyToManyField(Acessorio, related_name="veiculos")
    def __str__(self):
        return f"{self.modelo}, {self.cor}, {self.ano}"