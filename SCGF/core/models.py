from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Transacao(models.Model):

    STATUS = {
        ('pago', 'Pago'),
        ('nao_pago', 'Não Pago'),
    }

    TIPO = {
        ('despesa', 'Despesa'),
        ('receita', 'Receita'),
    }

    descricao = models.CharField(max_length=40)
    valor = models.FloatField()
    data_transacao = models.DateTimeField(verbose_name='Data da Transação')
    recorrencia = models.DecimalField(max_digits=5, decimal_places=0)

    pago = models.CharField(
        max_length=8,
        choices=STATUS,
    )

    tipo_transacao = models.CharField(
        max_length=7,
        choices=TIPO,
    )

    class Meta:
        db_table = 'transacao'

    def __str__(self):
        return self.descricao

    def get_data_transacao(self):
        return self.data_transacao.strftime('%d/%m/%Y %H:%M')
    
    def get_data_input_transacao(self):
        return self.data_transacao.strftime('%Y-%m-%dT%H:%M')
