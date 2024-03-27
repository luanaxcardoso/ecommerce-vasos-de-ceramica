from django.shortcuts import render, redirect
from .models import *
from .forms import PedidoForm
from django.contrib import messages


def home(request):
    produtos = Produto.objects.all()
    produto_list = Produto.objects.all()  
    return render(request, "home.html", {'produtos': produtos, 'produto_list': produto_list})


def sobre(request):
    return render(request, "sobre.html")

def contato(request):
    return render(request, "contato.html")

def pedido_order(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PedidoForm()
    return render(request, 'pedido_order.html', {'form': form})


def fazer_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.cliente = request.user.cliente  # Associando o cliente ao pedido

            # Obtendo ou criando o carrinho associado ao cliente
            carrinho, _ = Carrinho.objects.get_or_create(cliente=request.user.cliente)
            pedido.carrinho = carrinho

            pedido.save()
            form.save_m2m()  # Salvar os muitos-para-muitos, se houver
            messages.success(request, 'Pedido realizado com sucesso!')
            return redirect('pagina_sucesso_pedido')  # Redirecionar para a página de sucesso do pedido
    else:
        form = PedidoForm()
    return render(request, 'fazer_pedido.html', {'form': form})