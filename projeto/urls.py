#urls.py
from django.urls import path
from projeto.views import *



app_name = "projeto"
urlpatterns = [
    path('', home, name="home"),
    path('sobre/', sobre, name="sobre"),
    path('contato/', contato, name="contato"),
    path('pedido_order/', pedido_order, name='pedido_order'),
]
