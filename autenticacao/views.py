from django.shortcuts import redirect, redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.messages import constants

# Create your views here.


def cadastro(request):
    """view function para a página de cadastro"""
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/plataforma')
        return render(request, 'cadastro.html')
    elif request.method == 'POST':
        username = request.POST['username']  # ou request.POST.get('username')
        senha = request.POST['password']
        confirmar_senha = request.POST['confirm-password']

        if senha != confirmar_senha:
            messages.add_message(request, constants.ERROR, 'As senhas não coincidem.')
            return redirect('/auth/cadastro')

        if len(username) == 0 or len(senha) == 0:
            messages.add_message(request, constants.ERROR, 'Os campos não podem ficar vazios.')
            return redirect('/auth/cadastro')

        user = User.objects.filter(username=username)

        if user.exists():
            messages.add_message(request, constants.ERROR, 'Esse usuário já existe.')
            return redirect('/auth/cadastro')

        try:
            user = User.objects.create_user(username=username, password=senha)
            user.save()
            messages.add_message(request, constants.ERROR, 'Usuário criado com sucesso.')
            return redirect('/auth/logar')

        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema.')
            return redirect('/auth/cadastro')

def logar(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/plataforma')
        return render(request, 'logar.html')

    elif request.method == 'POST':
        username = request.POST['username']
        senha = request.POST['password']
        print(f'{username} | {senha}')
        
        usuario = auth.authenticate(username=username, password=senha)
        
        if not usuario:
            messages.add_message(request, constants.ERROR, 'Nome de usuário ou Senha inválidos')
            return redirect('/auth/logar')
        else:
            auth.login(request, usuario)
            return redirect('/plataforma')

def sair(request):
    auth.logout(request)
    return redirect('/auth/logar')
