from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse

from .getdata import getLinhaBase
from .getdata import getEvo


class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
       context = super(IndexView, self).get_context_data(**kwargs)
       context['graph'] = getLinhaBase()
       context['plot'] = getEvo()
       return context
