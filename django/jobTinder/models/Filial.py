from django.db import models


class Filial(models.Model):
    cnpj = models.CharField(max_length=50)
    endereco = models.ForeignKey("Endereco", on_delete=models.CASCADE)
    empresa = models.ForeignKey("Empresa", on_delete=models.CASCADE)

    def __init__(self, cnpj, endereco, empresa):
        self.cnpj = cnpj
        self.endereco = endereco
        self.empresa = empresa

    def __str__(self):
        return self.empresa.nome
    class Meta:
        app_label = 'jobTinder'