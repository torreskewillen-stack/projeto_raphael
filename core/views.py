from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

def produtos(request):
    return render(request, 'core/produtos.html')

def produto(request):
    return render(request, 'core/produto.html')

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
