from django import forms
from .models import Transacao, Grupo

class TransacaoForm(forms.ModelForm):
    class Meta:
        model = Transacao
        fields = ('descricao', 'valor', 'data_transacao', 'recorrencia', 'pago', 'tipo_transacao')

class GrupoForm(forms.ModelForm):
    class Meta:
        model = Grupo
        fields = ('nome', 'membros')