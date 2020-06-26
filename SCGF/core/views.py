from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Transacao, Grupo
from .forms import TransacaoForm, GrupoForm
from django.contrib import messages
from django.db.models import Sum

# Create your views here.

def home(request):
    transacoes = Transacao.objects.filter(user=request.user)
    receita = Grupo.soma_receita(transacoes)
    despesa = Grupo.soma_despesa(transacoes)

    return render(request, 'pages/home.html', {'transacoes': transacoes, 'receita': receita, 'despesa': despesa})

def group(request):
    grupo = Grupo.objects.last()
    membros = grupo.membros.all()
      
    receitas = Grupo.receita_membros(membros)
    despesas = Grupo.despesa_membros(membros)
    
    grupos = Grupo.objects.all()

    transacao = Transacao.objects.all()
    receita = Grupo.soma_receita(transacao)
    despesa = Grupo.soma_despesa(transacao)
        
    return render(request, 'pages/group.html', {'grupos': grupos, 'membros': membros, 'receitas': receitas, 'despesas': despesas, 'receita': receita, 'despesa': despesa})

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

def newGroup(request):
    if request.method == 'POST':
        form = GrupoForm(request.POST)
        
        if form.is_valid():
            grupo = form.save(commit=False)
            grupo.save()

            return redirect('group')
    else:
        form = GrupoForm()
        return render(request, 'pages/newgroup.html', {'form': form})