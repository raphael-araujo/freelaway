from django.shortcuts import redirect, redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants

# Create your views here.


def cadastro(request):
    """view function para a página de cadastro"""
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    elif request.method == 'POST':
        username = request.POST['username']  # ou request.POST.get('username')
        senha = request.POST['password']
        confirmar_senha = request.POST['confirm-password']
        # print(f'{username} | {senha} | {confirmar_senha}')

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
            return redirect('/auth/logar')

        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema.')
            return redirect('/auth/cadastro')

def logar(request):
    return HttpResponse('Logar')
