from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import *
from django.http import JsonResponse


def home(request):
    produtos = Produto.objects.all()
    produto_list = Produto.objects.all()  
    return render(request, "home.html", {'produtos': produtos, 'produto_list': produto_list})

def sobre(request):
    return render(request, "sobre.html")

def contato(request):
    return render(request, "contato.html")

def buscar_produtos(request):
    query = request.GET.get('q')
    resultados = Produto.objects.filter(nome_produto__icontains=query)
    produtos = [{'nome_produto': produto.nome_produto, 'descricao': produto.descricao} for produto in resultados]
    return JsonResponse(produtos, safe=False)

def produtos(request):
    produtos = Produto.objects.all()
    return render(request, "produtos.html", {'produtos': produtos})


def adicionar_carrinho(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    if 'carrinho_id' in request.session:
        carrinho_id = request.session['carrinho_id']
        carrinho = Carrinho.objects.get(id=carrinho_id)
    else:
        cliente = request.user.cliente  # Supondo que o cliente esteja autenticado
        carrinho = Carrinho.objects.create(cliente=cliente)
        request.session['carrinho_id'] = carrinho.id

    # Verificar se o produto já está no carrinho
    if CarrinhoProduto.objects.filter(carrinho=carrinho, produto=produto).exists():
        carrinho_produto = CarrinhoProduto.objects.get(carrinho=carrinho, produto=produto)
        carrinho_produto.quantidade += 1
        carrinho_produto.subtotal = carrinho_produto.quantidade * carrinho_produto.preco
        carrinho_produto.save()
    else:
        preco = produto.preco
        carrinho_produto = CarrinhoProduto.objects.create(carrinho=carrinho, produto=produto, quantidade=1, preco=preco, subtotal=preco)

    messages.success(request, f'{produto.nome_produto} foi adicionado ao carrinho.')
    return redirect('carrinho')

def remover_item_carrinho(request, carrinho_produto_id):
    carrinho_produto = get_object_or_404(CarrinhoProduto, id=carrinho_produto_id)
    carrinho_produto.delete()
    messages.success(request, 'Item removido do carrinho.')
    return redirect('carrinho')

def limpar_carrinho(request):
    if 'carrinho_id' in request.session:
        carrinho_id = request.session['carrinho_id']
        CarrinhoProduto.objects.filter(carrinho_id=carrinho_id).delete()
        messages.success(request, 'Carrinho esvaziado.')
    return redirect('carrinho')

def carrinho(request):
    if 'carrinho_id' in request.session:
        carrinho_id = request.session['carrinho_id']
        carrinho = Carrinho.objects.get(id=carrinho_id)
        itens_carrinho = CarrinhoProduto.objects.filter(carrinho=carrinho)
        total_carrinho = sum(item.subtotal for item in itens_carrinho)
    else:
        carrinho = None
        itens_carrinho = None
        total_carrinho = 0
    
    return render(request, 'carrinho.html', {'carrinho': carrinho, 'itens_carrinho': itens_carrinho, 'total_carrinho': total_carrinho})