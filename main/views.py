from django.contrib import admin
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


from .getdata import getLinhaBase
from .getdata import getEvo
from abastece.models import Cronograma

class BuscaPosto(ListView):
    template_name = 'main/search.html'
    model = Cronograma

    @method_decorator(login_required, name='dispatch')
    def dispatch(self, *args, **kwargs):
        return super(BuscaPosto, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(BuscaPosto, self).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        query = self.request.GET.get('posto_info')
        if len(query) == 4:
            return Cronograma.objects.filter(posto_cgmp__contains=query)
        else:
            return None



class IndexView(TemplateView):
    template_name = 'main/index.html'

    @method_decorator(login_required, name='dispatch')
    def dispatch(self, *args, **kwargs):
        return super(IndexView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
       context = super(IndexView, self).get_context_data(**kwargs)
       context['graph'] = getLinhaBase()
       context['plot'] = getEvo()
       return context

