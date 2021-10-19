from django.shortcuts import render
import requests


def index(request):
    return render(request, 'index.html')


def jogo(request):
    printar = {}
    if 'cep' in request.GET:
        cep = request.GET['cep']
        if cep != "":
            x = requests.get("https://viacep.com.br/ws/{}/json/".format(cep))
            printar = x.json()
        elif cep == "":
            printar = {'chave': 'Digite um cep valido'}

    return render(request, 'jogo.html', {'printar': printar})


def sobre(request):
    return render(request, 'sobre.html')