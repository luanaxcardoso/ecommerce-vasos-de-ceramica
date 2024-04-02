from django.urls import path
from usuarios.views import *
from projeto.views import *



urlpatterns = [
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('cadastro/', cadastro, name='cadastro'),
    path('logout/', logout, name='logout'),
    path('produtos/', produtos, name='produtos'),  
    path('carrinho/', carrinho, name='carrinho'),
]