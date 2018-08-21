from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('campanha.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now())
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

class Cidade(models.Model):
    nome = models.CharField(max_length=80)
    sigla = models.CharField(max_length=3)

    def __str__(self):
        return self.nome

def get_cidade_brasilia():
    return Cidade.objects.get_or_create(nome='Brasília',sigla='BSB')[0]

class Eleitor(models.Model):
    nome = models.CharField(max_length=80)
    telefone = models.IntegerField(max_length=15)
    cidade = models.ForeignKey('campanha.Cidade', on_delete=models.SET(get_cidade_brasilia), related_name='eleitores')
    origem = models.CharField(max_length=80)
    envio = models.BooleanField(default=False)
    usuario = models.ForeignKey('auth.user', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
