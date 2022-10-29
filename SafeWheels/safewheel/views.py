from asyncio.windows_events import NULL
from audioop import reverse
from http.client import HTTPResponse
from tkinter import Entry
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Estabelecimentos

def index(request):
    estabelecimentos = Estabelecimentos.objects.all
    return render(request, 'safewheel/index.html', {"estabelecimentos": estabelecimentos})

def login_user(request):
    if request.method == "GET":
        return render(request, 'safewheel/login.html')
    else:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            
            return redirect('index')
        else:
            return HttpResponse('Usuario não encontrado')
        

def mudaSenha(request):
    return render(request, 'safewheel/mudaSenha.html')

def esqueceuSenha(request):
    if request.method =="GET":
        return render(request, 'safewheel/esqueceuSenha.html')
    else: 
        email = request.POST.get('email')
    return HttpResponse('Email de confirmação foi enviado com sucesso para '+ str(email))

def cadastroEstabelecimento(request):
    if request.method =="GET":
        return render(request, 'safewheel/cadastroEstabelecimento.html')
    else:
        nomeE = request.POST.get('nomeE')
        local = request.POST.get('local')
        desc = request.POST.get('desc')
        imagens = request.FILES.get('imagens')
        Estabelecimentos.objects.create(nome=request.user, nomeE=nomeE, local=local, desc=desc, imagens=imagens)
        estabelecimentos = Estabelecimentos.objects.all()
        return render(request, 'safewheel/cadastroEstabelecimento.html', {"estabelecimentos": estabelecimentos})

def cadastroUsuario(request, id=NULL):
    if request.method == "GET":
        return render(request, 'safewheel/cadastroUsuario.html')
    else:
        username = request.POST.get('nome')
        email = request.POST.get('email')
        password = request.POST.get('senha1')   
        password2 = request.POST.get('senha2')

        user = User.objects.filter(username=username).first()

        if password != password2:
            return HttpResponse('Senha não estão iguais')
        if user:
            return HttpResponse('Já existe um usuario com este nome')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, f"Sua conta foi criada com sucesso, {username}")

            return redirect('login')


def detalhesEstabelecimentos(request, id):
    estabelecimentos = get_object_or_404(Estabelecimentos, id=id)
    return render(request, 'safewheel/detalhesEstabelecimentos.html', {"estabelecimentos": estabelecimentos})

def editarEstabelecimento(request, id):
    estabelecimento = Estabelecimentos.objects.get(id=id)
    return render(request, 'safewheel/editarEstabelecimento.html', {"estabelecimentos": estabelecimento})

def updateEstabelecimento(request, id):
    nomeE = request.POST.get('nomeE')
    local = request.POST.get('local')
    desc = request.POST.get('desc')
    imagens = request.FILES.get('imagens')

    estabelecimento = Estabelecimentos.objects.get(id=id)

    estabelecimento.nomeE = nomeE
    estabelecimento.local = local
    estabelecimento.desc = desc
    estabelecimento.imagens = imagens

    estabelecimento.save()

    return redirect('index')

def deletar(request, id):
    estabelecimento = get_object_or_404(Estabelecimentos, id=id)

    estabelecimento.delete()
    return redirect('index')