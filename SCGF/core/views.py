from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Transacao
from .forms import TransacaoForm
from django.contrib import messages
from django.db.models import Sum

# Create your views here.

def home(request):
    transacoes = Transacao.objects.filter(user=request.user)
    receita = Transacao.objects.filter(user=request.user, tipo_transacao='receita').aggregate(sum=Sum('valor'))['sum']
    despesa = Transacao.objects.filter(user=request.user, tipo_transacao='despesa').aggregate(sum=Sum('valor'))['sum']

    return render(request, 'pages/home.html', {'transacoes': transacoes, 'receita': receita, 'despesa': despesa})

def group(request):
    receita = Transacao.objects.filter(tipo_transacao='receita').aggregate(sum=Sum('valor'))['sum']
    despesa = Transacao.objects.filter(tipo_transacao='despesa').aggregate(sum=Sum('valor'))['sum']
    
    return render(request, 'pages/group.html', {'receita': receita, 'despesa': despesa})

def newTransaction(request):
    if request.method == 'POST':
        form = TransacaoForm(request.POST)
        
        if form.is_valid():
            transacao = form.save(commit=False)
            transacao.user = request.user
            transacao.save()

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