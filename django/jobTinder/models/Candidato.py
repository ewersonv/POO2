from django.db import models
from .Perfil import Perfil


class Candidato(Perfil):
    experiencia = models.CharField(max_length=280)
    habilidades = models.CharField(max_length=50)
    local_preferencia:str = models.CharField(max_length=50)

    def __init__(self, nome, cpf, email, senha, data_nascimento, experiencia, habilidades, local_preferencia):
        super().__init__(nome, cpf, email, senha, data_nascimento)
        self.experiencia = experiencia
        self.habilidades = habilidades
        self.local_preferencia = local_preferencia

    #def pesquisarVaga():

    def __str__(self):
        return super.nome
        
    class Meta:
        app_label = 'jobTinder'
