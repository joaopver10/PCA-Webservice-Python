from django.urls import path

from .views import index, jogo, sobre

urlpatterns = [
    path('', index, name='index'),
    path('Jogo', jogo, name='jogo'),
    path('Sobre', sobre, name='sobre')
]