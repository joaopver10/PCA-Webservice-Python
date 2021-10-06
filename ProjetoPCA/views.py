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
            printar = {'chave': 'Digite um cep valido'}

    return render(request, 'index.html', {'printar': printar})


