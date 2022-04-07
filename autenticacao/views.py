from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def cadastro(request):
    """view function para a página de cadastro"""
    return render(request, 'cadastro.html')

def logar(request):
    return HttpResponse('Logar')
