from django.db import models
from .Mensagem import Mensagem

class Observador(models.Models):
    #Alerta o status
    def update(self,msg: Mensagem):
        if(msg.statusRemetente == 'Não lida'):
            print("Mensagem foi lida")
            msg.status('lida')
        return

    class Meta:
        app_label = 'jobTinder'