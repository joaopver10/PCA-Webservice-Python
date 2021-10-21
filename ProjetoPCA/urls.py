from django.urls import path

from .views import index, jogo, sobre

urlpatterns = [
    path('', index, name='index'),
    path('Curiosidades', jogo, name='curiosidades'),
    path('Sobre', sobre, name='sobre')
]