from django import forms
from .models import *


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido_order
        fields = ['cliente','subtotal', 'total',  'pedido_status', 'observacoes', 'endereco_envio', 'telefone', 'email']

    widgets = {
        'cliente': forms.TextInput(attrs={'class': 'form-control'}),
        'subtotal': forms.NumberInput(attrs={'class': 'form-control'}),
        'total': forms.NumberInput(attrs={'class': 'form-control'}),
        'pedido_status': forms.Select(attrs={'class': 'form-control'}),
        'observacoes': forms.Textarea(attrs={'class': 'form-control'}),
        'endereco_envio': forms.TextInput(attrs={'class': 'form-control'}),
        'telefone': forms.TextInput(attrs={'class': 'form-control'}),
        'email': forms.EmailInput(attrs={'class': 'form-control'}),
    }


class CarrinhoProdutoForm(forms.ModelForm):
    class Meta:
        model = CarrinhoProduto
        fields = ['carrinho', 'produto', 'quantidade', 'preco', 'avaliacao', 'subtotal']

    widgets = {
        'carrinho': forms.Select(attrs={'class': 'form-control'}),
        'produto': forms.Select(attrs={'class': 'form-control'}),
        'quantidade': forms.NumberInput(attrs={'class': 'form-control'}),
        'preco': forms.NumberInput(attrs={'class': 'form-control'}),
        'avaliacao': forms.NumberInput(attrs={'class': 'form-control'}),
        'subtotal': forms.NumberInput(attrs={'class': 'form-control'}),
    }
