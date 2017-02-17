from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse

from .getdata import getKPIs


class IndexView(TemplateView):
    template_name = 'abastece/index.html'

    def get_context_data(self, **kwargs):
        context = super(Acumulado, self).get_context_data(**kwargs)
        context['graph'] = getAtendimentoAcumulados('1')
        return context
