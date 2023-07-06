from django.db import models

# Será transformado em uma tabela no banco de dados

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True) # criando um campo número que vai gerar um número sequêncial
    nome = models.TextField(max_length=255)
    idade = models.IntegerField()

