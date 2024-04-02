from django.urls import path
from projeto.views import *

app_name = "projeto"
urlpatterns = [
    path('', home, name="home"),
    path('sobre/', sobre, name="sobre"),
    path('contato/', contato, name="contato"),
    path('buscar/', buscar_produtos, name='buscar_produtos'),
    path('produtos/', produtos, name='produtos'),  
    path('carrinho/', carrinho, name='carrinho'),
   

]
