from django.db import models
from django.contrib.auth import get_user_model
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

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        db_table = 'transacao'

    def __str__(self):
        return self.descricao

    def get_data_transacao(self):
        return self.data_transacao.strftime('%d/%m/%Y')
    
    def get_data_input_transacao(self):
        return self.data_transacao.strftime('%Y-%m-%d')


class Grupo(models.Model):
    nome = models.CharField(max_length=40)

    membros = models.ManyToManyField(get_user_model())

    class Meta:
        db_table = 'grupo'

    def soma_receita(self):
        receita = 0
        for x in self:
            if x.tipo_transacao == 'receita':
                receita += x.valor
        return receita

    def soma_despesa(self):
        despesa = 0
        for x in self:
            if x.tipo_transacao == 'despesa':
                despesa += x.valor
        return despesa

    def receita_membros(self):
        result = 0
        lista = []
        for membro in self:
            transacoes = Transacao.objects.filter(user=membro)
            result = Grupo.soma_receita(transacoes)
            lista.append(result)
        return lista

    def despesa_membros(self):
        result = 0
        lista = []
        for membro in self:
            transacoes = Transacao.objects.filter(user=membro)
            result = Grupo.soma_despesa(transacoes)
            lista.append(result)
        return lista