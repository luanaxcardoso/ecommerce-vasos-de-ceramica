from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

def login(request):
    form = LoginForms()
    
    if request.method == "POST":
        form = LoginForms(request.POST)
         
        if form.is_valid(): 
            nome = form.cleaned_data["nome_login"]
            senha = form.cleaned_data["senha"]
            
            usuario = auth.authenticate(request, username=nome, password=senha)  
            
            if usuario is not None:
                auth.login(request, usuario)
                messages.success(request, "Login efetuado com sucesso")
                return redirect('produtos')  
            else:  
                messages.error(request, "Login inválido")      
                return redirect('login')     

    return render(request, "login.html", {"form": form})

def cadastro(request):
    form = CadastroForms()
    
    if request.method == "POST":
        form = CadastroForms(request.POST)   
        
        if form.is_valid():
            nome = form.cleaned_data["nome_cadastro"]
            email = form.cleaned_data["email"]
            senha = form.cleaned_data["senha_1"]
            
            if User.objects.filter(username=nome).exists():
                messages.error(request, "Usuário já cadastrado")       
                return redirect('cadastro')  # Redireciona de volta para o formulário de cadastro se o usuário já existir

            usuario = User.objects.create_user(
                username=nome, 
                email=email, 
                password=senha)
            usuario.save()
            messages.success(request, "Cadastro efetuado com sucesso")
            return redirect('login')  # Redireciona para a página de login após o cadastro

    return render(request, "cadastro.html", {"form": form})

def logout(request):
    messages.success(request, "Logout efetuado com sucesso")
    auth.logout(request)
    return redirect('login')  # Redireciona para a página de login após o logout
