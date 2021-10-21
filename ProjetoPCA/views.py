from django.shortcuts import render
import requests
from .models import Estados


def index(request):
    return render(request, 'index.html')


def jogo(request):
    printar = {}
    try:
        if 'cep' in request.GET:
            cep = request.GET['cep']
            x = requests.get("https://viacep.com.br/ws/{}/json/".format(cep))
            cepJ = x.json()
            estados = Estados.objects.filter(sigla=cepJ['uf'])
            if estados:
                printar = {'estados': estados}
    except ValueError:
        printar = {'erro': 'O cep digitado está errado ou ainda não temos a historia desse estado adicionado no nosso banco de dados.'}

    return render(request, 'jogo.html', printar)


def sobre(request):
    return render(request, 'sobre.html')