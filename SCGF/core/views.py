from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Transacao
from .forms import TransacaoForm
from django.contrib import messages
from django.db.models import Count, Sum

# Create your views here.

def home(request):
    transacoes = Transacao.objects.all()
    return render(request, 'pages/home.html', {'transacoes': transacoes})

def group(request):
    total = Transacao.objects.aggregate(sum_total=Sum('valor'))
    receita = Transacao.objects.filter(tipo_transacao='receita').aggregate(Sum('valor'))
    despesa = Transacao.objects.filter(tipo_transacao='despesa').aggregate(Sum('valor'))
    
    return render(request, 'pages/group.html', { 'receita': receita, 'despesa': despesa, 'total': total})

def newTransaction(request):
    if request.method == 'POST':
        form = TransacaoForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TransacaoForm()
        return render(request, 'pages/addTransaction.html', {'form': form})

def editTransaction(request, id):
    transacao = get_object_or_404(Transacao, pk=id)
    form = TransacaoForm(instance=transacao)

    if(request.method == 'POST'):
        form = TransacaoForm(request.POST, instance=transacao)

        if(form.is_valid()):
            transacao.save()
            return redirect('/')
        else:
            return render(request, 'pages/editTransaction.html', {'form': form, 'transacao': transacao})

    else:
        return render(request, 'pages/editTransaction.html', {'form': form, 'transacao': transacao})

def deleteTransaction(request, id):
    transacao = get_object_or_404(Transacao, pk=id)
    transacao.delete()

    messages.info(request, 'Transação deletada com sucesso.')

    return redirect('/')