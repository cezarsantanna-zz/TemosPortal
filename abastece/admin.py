from django.contrib import admin
from datetime import datetime
from .models import Form
from .models import Empresa
from .models import Classe
from .models import Employee
from .models import ModeloViatura
from .models import Viatura
from .models import Warehouse
from .models import Base
from .models import ModeloEquipamento
from .models import Equipamento
from .models import Posto
from .models import TipoEvento
from .models import Evento
from .models import Punch

# Definção de exibição no Admin
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

# Register your models here.
admin.site.register(Form)
admin.site.register(Empresa)
admin.site.register(Classe)
admin.site.register(Employee)
admin.site.register(ModeloViatura)
admin.site.register(Viatura)
admin.site.register(Warehouse)
admin.site.register(Base)
admin.site.register(ModeloEquipamento)
admin.site.register(Equipamento)
admin.site.register(Posto)
admin.site.register(TipoEvento)
admin.site.register(Evento)
admin.site.register(Punch, PunchAdmin)
