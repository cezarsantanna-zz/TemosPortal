from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse

from .getdata import getAtendimentoAcumulados
from .getdata import getAtendimentoDia


class IndexView(TemplateView):
    template_name = 'abastece/index.html'

def detail(request, posto__cgmp):
    return HttpResponse("%s" % posto__cgmp)

def eventos(request, posto__cgmp):
    return HttpResponse("%s" % posto__cgmp)

class Acumulado(TemplateView):
    template_name = 'abastece/acumulado.html'

    def get_context_data(self, **kwargs):
        context = super(Acumulado, self).get_context_data(**kwargs)
        context['graph'] = getAtendimentoAcumulados('1')
        return context

class Diario(TemplateView):
    template_name = 'abastece/diario.html'

    def get_context_data(self, **kwargs):
        context = super(Diario, self).get_context_data(**kwargs)
        context['graph'] = getAtendimentoDia('1')
        return context
