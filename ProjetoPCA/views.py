from django.shortcuts import render
import requests


def index(request):
    printar = {}
    if 'cep' in request.GET:
        cep = request.GET['cep']
        if cep != "":
            x = requests.get("https://viacep.com.br/ws/{}/json/".format(cep))
            printar = x.json()
        elif cep == "":
            printar = {'chave': 'Error digite um cep valido'}

    return render(request, 'index.html', {'printar': printar})


def contato(request):
    return render(request, 'contato.html')