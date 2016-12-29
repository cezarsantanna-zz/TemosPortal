from django.db import models

class Form(models.Model):
    active = models.BooleanField(default=True)
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Empresa(models.Model):
    active = models.BooleanField(default=True)
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Warehouse(models.Model):
    active = models.BooleanField(default=True)
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Classe(models.Model):
    CLASSES = (
        ('A', 'Posto com ótima classificação'),
        ('B', 'Posto com boa classificação'),
        ('C', 'Posto com média classificação'),
        ('D', 'Posto com baixa classificação'),
    )
    name = models.CharField(max_length=1, choices=CLASSES)

    def __str__(self):
        return self.name


class Employee(models.Model):
    active = models.BooleanField(default=True)
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class ModeloViatura(models.Model):
    active = models.BooleanField(default=True)
    name = models.CharField(max_length=20)
    km_rev = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Viatura(models.Model):
    active = models.BooleanField(default=True)
    placa = models.CharField(max_length=7)
    celular = models.CharField(max_length=11)
    coordx = models.CharField(max_length=20)
    coordy = models.CharField(max_length=20)
    quilometragem = models.PositiveIntegerField()
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)
    modeloviatura = models.ForeignKey(ModeloViatura, on_delete=models.PROTECT)

    def __str__(self):
        return self.placa


class Base(models.Model):
    active = models.BooleanField(default=True)
    name = models.CharField(max_length=5)
    coordx = models.CharField(max_length=20)
    coordy = models.CharField(max_length=20)
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)
    viatura = models.ForeignKey(Viatura, on_delete=models.PROTECT)
    warehouse = models.OneToOneField(Warehouse, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class NomeItem(models.Model):
    active = models.BooleanField(default=True)
    name = models.CharField(max_length=80)
    model = models.CharField(max_length=40, null=True)
    maker = models.CharField(max_length=45, null=True)
    width = models.FloatField(null=True)
    height = models.FloatField(null=True)
    depth = models.FloatField(null=True)
    prazocompra = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class ItemControlado(models.Model):
    identificador = models.CharField(max_length=16, primary_key=True)
    serial = models.CharField(max_length=80, null=True)
    assetnumber = models.CharField(max_length=80, null=True)
    nomeitem = models.ForeignKey(NomeItem, on_delete=models.PROTECT)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.PROTECT)

    def __str__(self):
        return self.identificador


class MoveItem(models.Model):
    timestamp = models.DateField(auto_now_add=True)
    warehouse_origin = models.ForeignKey(Warehouse, on_delete=models.PROTECT)
    warehouse_dest = models.ForeignKey(Warehouse, on_delete=models.PROTECT)


class Inventory(models.Model):
    entrydate = models.PositiveIntegerField()
    warehouse = models.ForeignKey(Warehouse, on_delete=models.PROTECT)
    nomeitem = models.ForeignKey(NomeItem, on_delete=models.PROTECT)
    item_new = models.IntegerField()
    item_used = models.IntegerField()
    item_broaked = models.IntegerField()


class Posto(models.Model):
    active = models.BooleanField(default=True)
    name = models.CharField(max_length=60)
    cgmp = models.CharField(max_length=5)
    status_opc = models.BooleanField()
    status_vip = models.BooleanField()
    coordx = models.CharField(max_length=20)
    coordy = models.CharField(max_length=20)
    classe = models.ForeignKey(Classe, on_delete=models.PROTECT)
    base = models.ForeignKey(Base, on_delete=models.PROTECT)
    warehouse = models.OneToOneField(Warehouse, on_delete=models.PROTECT)

    def __str__(self):
        return self.cgmp


class TipoEvento(models.Model):
    active = models.BooleanField(default=True)
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Evento(models.Model):
    active = models.BooleanField(default=True)
    data_planejado = models.PositiveIntegerField()
    data_realizado = models.PositiveIntegerField()
    number = models.CharField(max_length=20)
    resumo = models.TextField(null=True)
    posto = models.ForeignKey(Posto, on_delete=models.PROTECT)
    base = models.ForeignKey(Base, on_delete=models.PROTECT)
    employee = models.ForeignKey(Employee, null=True, on_delete=models.PROTECT)
    form = models.ForeignKey(Form, on_delete=models.PROTECT)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)

    def __str__(self):
        return self.number


class Tarefa(models.Model):
    active = models.BooleanField(default=True)
    number = models.CharField(max_length=10, unique=True)
    posto = models.ForeignKey(Posto, on_delete=models.PROTECT)
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)
    status = models.IntegerField()
    description = models.CharField(max_length=20)
    name = models.CharField(max_length=45)
    start_date = models.PositiveIntegerField(null=True)
    end_date = models.PositiveIntegerField(null=True)
    start_coordx = models.CharField(max_length=20)
    start_coordy = models.CharField(max_length=20)
    end_coordx = models.CharField(max_length=20)
    end_coordy = models.CharField(max_length=20)


class Punch(models.Model):
    active = models.BooleanField(default=True)
    in_time = models.PositiveIntegerField(null=True)
    out_time = models.PositiveIntegerField(null=True)
    entry_date = models.DateField(default='1970-01-01')
    in_coordx = models.CharField(max_length=20, null=True)
    in_coordy = models.CharField(max_length=20, null=True)
    out_coordx = models.CharField(max_length=20, null=True)
    out_coordy = models.CharField(max_length=20, null=True)
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)

    def __str__(self):
        return self.entry_date
