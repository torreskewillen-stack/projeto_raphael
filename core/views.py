from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

def produtos(request):
    return render(request, 'core/produtos.html')

def produto(request):
    return render(request, 'core/produto.html')

def carrinho(request):
    return render(request, 'core/carrinho.html')