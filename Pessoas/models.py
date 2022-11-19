from django.db import models
from django.contrib.auth.models import User



class Pessoa(models.Model):
    
    nome_completo = models.CharField(max_length=256)
    data_nascimento = models.DateField(null=True)
    ativa = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self.nome_completo
    



class Contato(models.Model): 

    nome = models.CharField(max_length=256, default='Contato próprio')
    email = models.EmailField(max_length=256)
    telefone = models.CharField(max_length=20)
    pessoa = models.ForeignKey(Pessoa, related_name='contatos',on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nome