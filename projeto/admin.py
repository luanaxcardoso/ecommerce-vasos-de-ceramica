from django.contrib import admin
from .models import *

admin.site.register(Cliente)
admin.site.register(Categoria)
admin.site.register(Produto)
admin.site.register(Carrinho)
admin.site.register(CarrinhoProduto)
admin.site.register(Pedido_order)