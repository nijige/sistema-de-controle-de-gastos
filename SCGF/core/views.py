from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Transacao
from .forms import TransacaoForm

# Create your views here.

def home(request):
    transacoes = Transacao.objects.all()
    return render(request, 'pages/home.html', {'transacoes': transacoes})

def group(request):
    return render(request, 'pages/group.html')

def newTransaction(request):
    if request.method == 'POST':
        form = TransacaoForm(request.POST)
        
        if form.is_valid():
            transacao = form.save()
            return redirect('/')
    else:
        form = TransacaoForm()
        return render(request, 'pages/addTransaction.html', {'form': form})