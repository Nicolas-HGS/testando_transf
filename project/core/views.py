from django.http import HttpResponse
from django.shortcuts import render

from .models import Topic


def index(request):
    Topic.objects.create(
        texto='texto',
        nome='topico1'
    )
    return HttpResponse('VIEW DO CORE')


def lista_topicos(request):
    topicos = Topic.objects.all()
    return render(request, 'core/lista.html', context={'nicolas': topicos})
