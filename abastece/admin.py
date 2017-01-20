from django.contrib import admin
from datetime import datetime
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

# Definção de exibição no Admin
class PostoAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'cgmp',
        'status_opc',
        'status_vip',
        'coordx',
        'coordy',
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
    )
    list_filter = (
        'form',
        'empresa',
    )
    search_fields = (
        'posto__name',
        'posto__cgmp',
    )

    ordering = ['entry_date', 'posto']

    date_hierarchy = 'entry_date'


    def get_posto_name(self, obj):
        return obj.posto.name
    get_posto_name.admin_order_field = 'posto'
    get_posto_name.short_description = 'Posto'

    def planejado(self, obj):
        if obj.data_planejado is None:
            return None
        else:
            return datetime.fromtimestamp(float(obj.data_planejado)).strftime('%d/%m/%Y %H:%M:%S')
    def realizado(self, obj):
        if obj.data_realizado is None:
            return None
        else:
            return datetime.fromtimestamp(float(obj.data_realizado)).strftime('%d/%m/%Y %H:%M:%S')


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
