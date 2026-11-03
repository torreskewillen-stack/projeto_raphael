from django.shortcuts import render, get_object_or_404
from .models import Produto

def home(request):
    produtos = Produto.objects.filter(ativo=True,destaque=True )
    return render(request, 'core/home.html', {'produtos': produtos})

def produtos(request):
    lista_produtos = Produto.objects.filter(ativo=True)
    return render(request, 'core/produtos.html',{'produtos': lista_produtos})

def produto(request, id):
    produto = get_object_or_404(Produto, id=id, ativo=True)
    return render(request, 'core/produto.html', {'produto': produto})

def carrinho(request):
    return render(request, 'core/carrinho.html')

def login_usuario(request):
    return render(request, 'core/login.html')

def cadastro(request):
    return render(request, 'core/cadastro.html')

def conta(request):
    return render(request, 'core/conta.html')

def contato(request):
    return render(request, 'core/contato.html')