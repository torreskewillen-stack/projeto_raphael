from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('produtos/', views.produtos, name='produtos'),
    path('produto/', views.produto, name='produto'),
    path('carrinho/', views.carrinho, name='carrinho'),
    path('login/', views.login_usuario, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('conta/', views.conta, name='conta'),
    path('contato/', views.contato, name='contato'),
]