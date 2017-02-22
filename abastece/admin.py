from django.contrib import admin
from datetime import datetime
from datetime import date
from .models import Form
from .models import Empresa
from .models import Employee
from .models import ModeloViatura
from .models import Viatura
from .models import Warehouse
from .models import Classe
from .models import Base
from .models import Item
from .models import ItemControlado
from .models import Posto
from .models import Evento
from .models import Punch
from .models import LinhaBase
from .models import Cronograma

# Definção de exibição no Admin
class PostoAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'cgmp',
        'status_opc',
        'status_vip',
        'getLatitude',
        'getLongitude',
        'classe',
        'base',
        'warehouse',
    )
    list_filter = (
        'classe',
        'status_vip',
        'status_opc',
    )
    search_fields = (
        'name',
        'cgmp',
    )

    def getLatitude(self, obj):
        return obj.coordy
    getLatitude.short_description = 'Latitude'

    def getLongitude(self, obj):
        return obj.coordx
    getLongitude.short_description = 'Longitude'


class PunchAdmin(admin.ModelAdmin):
    list_display = (
        'employee',
        'entry_date',
        'inTime',
        'outTime',
        'in_coordx',
        'in_coordy',
        'out_coordx',
        'out_coordy',
    )

    date_hierarchy = 'entry_date'

    def inTime(self, obj):
        if obj.in_time is None:
            return None
        else:
            return datetime.fromtimestamp(float(obj.in_time)).strftime('%d/%m/%Y %H:%M:%S')
    def outTime(self, obj):
        if obj.out_time is None:
            return None
        else:
            return datetime.fromtimestamp(float(obj.out_time)).strftime('%d/%m/%Y %H:%M:%S')


class LinhaBaseAdmin(admin.ModelAdmin):
    model = LinhaBase
    list_display = (
        'data_entrada',
        'preventiva',
        'as_built',
        'plano_verao',
        'preditiva',
        'retirada58',
        'antena915',
        'sinal',
        'outro',
        'icr',
        'suporte_angular',
        'posto_ok'
    )
    ordering = ['data_entrada']
    date_hierarchy = 'data_entrada'


class CronogramaAdmin(admin.ModelAdmin):
    model = Cronograma
    list_display = (
        'data_entrada',
        'posto',
        'get_posto_name',
        'get_status_preventiva',
        'get_status_asbuilt',
        'get_status_plano_verao',
        'get_status_preditiva',
        'get_status_retirada58',
        'get_status_antena915',
        'get_status_sinal',
        'get_status_outro',
        'get_status_icr',
        'get_status_suporte_angular'
    )
    search_fields = (
        'posto__name',
        'posto__cgmp'
    )
    ordering = ['data_entrada', 'posto']
    date_hierarchy = 'data_entrada'

    def get_posto_name(self, obj):
        return obj.posto.name
    get_posto_name.admin_order_field = 'posto'
    get_posto_name.short_description = 'Nome do posto'

    def get_status_preventiva(self, obj):
        if obj.preventiva is None:
            return None
        else:
            linha_corte = date(year=2016, month=12, day=31)
            if obj.preventiva == linha_corte:
                return 'OK'
            else:
                return obj.preventiva
    get_status_preventiva.admin_order_field = 'preventiva'
    get_status_preventiva.short_description = 'Preventiva'

    def get_status_asbuilt(self, obj):
        if obj.asbuilt is None:
            return None
        else:
            linha_corte = date(year=2016, month=12, day=31)
            if obj.asbuilt == linha_corte:
                return 'OK'
            else:
                return obj.asbuilt
    get_status_asbuilt.admin_order_field = 'asbuilt'
    get_status_asbuilt.short_description = 'As Built'

    def get_status_plano_verao(self, obj):
        if obj.plano_verao is None:
            return None
        else:
            linha_corte = date(year=2016, month=12, day=31)
            if obj.plano_verao == linha_corte:
                return 'OK'
            else:
                return obj.plano_verao
    get_status_plano_verao.admin_order_field = 'plano_verao'
    get_status_plano_verao.short_description = 'Plano Verão'

    def get_status_preditiva(self, obj):
        if obj.preditiva is None:
            return None
        else:
            linha_corte = date(year=2016, month=12, day=31)
            if obj.preditiva == linha_corte:
                return 'OK'
            else:
                return obj.preditiva
    get_status_preditiva.admin_order_field = 'preditiva'
    get_status_preditiva.short_description = 'Preditiva'

    def get_status_retirada58(self, obj):
        if obj.retirada58 is None:
            return None
        else:
            linha_corte = date(year=2016, month=12, day=31)
            if obj.retirada58 == linha_corte:
                return 'OK'
            else:
                return obj.retirada58
    get_status_retirada58.admin_order_field = 'retirada58'
    get_status_retirada58.short_description = 'Retirada 5.8'

    def get_status_antena915(self, obj):
        if obj.antena915 is None:
            return None
        else:
            linha_corte = date(year=2016, month=12, day=31)
            if obj.antena915 == linha_corte:
                return 'OK'
            else:
                return obj.antena915
    get_status_antena915.admin_order_field = 'antena915'
    get_status_antena915.short_description = 'Ajuste Antena 915'

    def get_status_sinal(self, obj):
        if obj.sinal is None:
            return None
        else:
            linha_corte = date(year=2016, month=12, day=31)
            if obj.sinal == linha_corte:
                return 'OK'
            else:
                return obj.sinal
    get_status_sinal.admin_order_field = 'sinal'
    get_status_sinal.short_description = 'Sinalização'

    def get_status_outro(self, obj):
        if obj.outro is None:
            return None
        else:
            linha_corte = date(year=2016, month=12, day=31)
            if obj.outro == linha_corte:
                return 'OK'
            else:
                return obj.outro
    get_status_outro.admin_order_field = 'outro'
    get_status_outro.short_description = 'Outro'

    def get_status_icr(self, obj):
        if obj.icr is None:
            return None
        else:
            linha_corte = date(year=2016, month=12, day=31)
            if obj.icr == linha_corte:
                return 'OK'
            else:
                return obj.icr
    get_status_icr.admin_order_field = 'icr'
    get_status_icr.short_description = 'ICR'

    def get_status_suporte_angular(self, obj):
        if obj.suporte_angular is None:
            return None
        else:
            linha_corte = date(year=2016, month=12, day=31)
            if obj.suporte_angular == linha_corte:
                return 'OK'
            else:
                return obj.suporte_angular
    get_status_suporte_angular.admin_order_field = 'suporte_angular'
    get_status_suporte_angular.short_description = 'Suporte Angular'


class EventoAdmin(admin.ModelAdmin):
    model = Evento
    list_display= (
        'posto',
        'get_posto_name',
        'form',
        'number',
        'planejado',
        'realizado',
        'empresa',
        'is_finished',
    )
    list_filter = (
        'form',
        'empresa',
    )
    search_fields = (
        'posto__name',
        'posto__cgmp',
        'number',
    )

    ordering = ['entry_date', 'posto',]

    date_hierarchy = 'entry_date'


    def get_posto_name(self, obj):
        return obj.posto.name
    get_posto_name.admin_order_field = 'posto'
    get_posto_name.short_description = 'Posto'

    def planejado(self, obj):
        if obj.data_planejado is None:
            return None
        else:
            planejado = datetime.utcfromtimestamp(
                float(obj.data_planejado)).strftime('%d/%m/%Y %H:%M:%S')
            return planejado
    planejado.short_description = ('Planejada para')
    planejado.admin_order_field = 'data_planejado'


    def realizado(self, obj):
        if obj.data_realizado is None:
            return None
        else:
            realizado = datetime.utcfromtimestamp(
                float(obj.data_realizado)).strftime('%d/%m/%Y %H:%M:%S')
            return realizado
    realizado.short_description = ('Realizada em')
    realizado.admin_order_field = 'data_realizado'

    def is_finished(self, obj):
        if obj.data_realizado is None:
            return False
        else:
            return True
    is_finished.short_description = ('Encerrado')
    is_finished.admin_order_field = ('data_realizado')
    is_finished.boolean = True


# Register your models here.
admin.site.register(Form)
admin.site.register(Empresa)
admin.site.register(Classe)
admin.site.register(Employee)
admin.site.register(ModeloViatura)
admin.site.register(Viatura)
admin.site.register(Warehouse)
admin.site.register(Base)
admin.site.register(Item)
admin.site.register(ItemControlado)
admin.site.register(Posto, PostoAdmin)
admin.site.register(Evento, EventoAdmin)
admin.site.register(Punch, PunchAdmin)
admin.site.register(LinhaBase, LinhaBaseAdmin)
admin.site.register(Cronograma, CronogramaAdmin)
