from django.db import models


class Estados(models.Model):
    sigla = models.CharField('Sigla', max_length=2)
    descricao = models.TextField('Descrição')

    def __str__(self):
        return self.sigla