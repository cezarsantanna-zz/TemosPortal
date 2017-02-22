from django.views.generic import TemplateView
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse

from .getdata import getLinhaBase
from .getdata import getEvo
from abastece.models import Cronograma

def buscaPosto(request):
    posto_info = request.GET.get('posto_info')
    nomes = Cronograma.objects.filter(name__contains=posto_info)
    cgmp = Cronograma.objects.filter(cgmp__contains=posto_info)
    p = getVariables(request)
    p['nomes'] = nomes
    p['cgmp'] = cgmp
    return render_to_response('search.html',p)

class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
       context = super(IndexView, self).get_context_data(**kwargs)
       context['graph'] = getLinhaBase()
       context['plot'] = getEvo()
       return context
