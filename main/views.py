from django.contrib import admin
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse

from .getdata import getLinhaBase
from .getdata import getEvo
from abastece.models import Cronograma


class BuscaPosto(ListView):
    template_name = 'main/search.html'
    model = Cronograma

    # 6 antena915,2 asbuilt,9 icr, id,8 outro,3 plano_verao, posto_cgmp, posto_nome,4 preditiva,1 preventiva,5 retirada58, 7 sinal, 10 suporte_angular

    # define the function blocks
    def funcPreventivas():
        return 'preventiva__icontains'
    
    def numbers_to_strings(argument):
        switcher = {
            0: "zero",
            1: "one",
            2: "two",
        }
        return switcher.get(argument, "nothing")

    def get_context_data(self, **kwargs):
        context = super(BuscaPosto, self).get_context_data(**kwargs)
        return context

    def get_queryset(self):

       # print numbers_to_strings(0)

        query = self.request.GET.get('posto_info')
        
        typeID = self.request.GET.get('typeID')
        if typeID == '':
            typeID = '-1'
        
        fOK = self.request.GET.get('fOK')
        if fOK == '':
            fOK = '0'
            
        if int(typeID) >= 0:
                if int(typeID) == 1:
                    if int(fOK) == 0:
                        return Cronograma.objects.filter(preventiva__icontains='OK')
                    else:
                        return Cronograma.objects.exclude(preventiva__icontains='OK')

                if int(typeID) == 2:
                    if int(fOK) == 0:
                        return Cronograma.objects.filter(asbuilt__icontains='OK')
                    else:
                        return Cronograma.objects.exclude(asbuilt__icontains='OK')
                    
                if int(typeID) == 3:
                    if int(fOK) == 0:
                        return Cronograma.objects.filter(plano_verao__icontains='OK')
                    else:
                        return Cronograma.objects.exclude(plano_verao__icontains='OK')

                if int(typeID) == 4:
                    if int(fOK) == 0:
                        return Cronograma.objects.filter(preditiva__icontains='OK')
                    else:
                        return Cronograma.objects.exclude(preditiva__icontains='OK')

                if int(typeID) == 5:
                    if int(fOK) == 0:
                        return Cronograma.objects.filter(retirada58__icontains='OK')
                    else:
                        return Cronograma.objects.exclude(retirada58__icontains='OK')
                    
                if int(typeID) == 6:
                    if int(fOK) == 0:
                        return Cronograma.objects.filter(antena915__icontains='OK')
                    else:
                        return Cronograma.objects.exclude(antena915__icontains='OK')
                    
                if int(typeID) == 7:
                    if int(fOK) == 0:
                        return Cronograma.objects.filter(sinal__icontains='OK')
                    else:
                        return Cronograma.objects.exclude(sinal__icontains='OK')

                if int(typeID) == 8:
                    if int(fOK) == 0:
                        return Cronograma.objects.filter(outro__icontains='OK')
                    else:
                        return Cronograma.objects.exclude(outro__icontains='OK')
                    
                if int(typeID) == 9:
                    if int(fOK) == 0:
                        return Cronograma.objects.filter(icr__icontains='OK')
                    else:
                        return Cronograma.objects.exclude(icr__icontains='OK')
                    
                if int(typeID) == 10:
                    if int(fOK) == 0:
                        return Cronograma.objects.filter(suporte_angular__icontains='OK')
                    else:
                        return Cronograma.objects.exclude(suporte_angular__icontains='OK')
                
                
        #Consulta por codigo do posto
        if len(query) == 4:
            return Cronograma.objects.filter(posto_cgmp__contains=query)
        else:
            return None


class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
       context = super(IndexView, self).get_context_data(**kwargs)
       context['graph'] = getLinhaBase()
       context['plot'] = getEvo()
       return context
