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
        'posto_cgmp',
        'posto_nome',
        'preventiva',
        'asbuilt',
        'plano_verao',
        'preditiva',
        'retirada58',
        'antena915',
        'sinal',
        'outro',
        'icr',
        'suporte_angular'
    )
    search_fields = (
        'posto_nome',
        'posto_cgmp'
    )
    ordering = ['posto_cgmp']


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
