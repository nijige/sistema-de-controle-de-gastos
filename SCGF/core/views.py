from django.shortcuts import render
from django.http import HttpResponse
from .models import Transacao

# Create your views here.

def home(request):
    transacoes = Transacao.objects.all()
    return render(request, 'pages/home.html', {'transacoes': transacoes})

def group(request):
    return render(request, 'pages/group.html')