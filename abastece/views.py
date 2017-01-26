from django.shortcuts import render
from django.http import HttpResponse
from .getdata import getAtendimentoAcumulados
from .getdata import getAtendimentoDia


def index(request):
    return render(request, 'abastece/index.html')
