from django.db import models

class Form(models.Model):
    active = models.BooleanField()
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Empresa(models.Model):
    active = models.BooleanField()
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Warehouse(models.Model):
    active = models.BooleanField()
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
    active = models.BooleanField()
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class ModeloViatura(models.Model):
    active = models.BooleanField()
    name = models.CharField(max_length=15)
    km_rev = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Viatura(models.Model):
    active = models.BooleanField()
    placa = models.CharField(max_length=7)
    celular = models.CharField(max_length=11)
    coordX = models.CharField(max_length=15)
    coordY = models.CharField(max_length=15)
    quilometragem = models.PositiveIntegerField()
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)
    modeloviatura = models.ForeignKey(ModeloViatura, on_delete=models.PROTECT)

    def __str__(self):
        return self.placa


class Base(models.Model):
    active = models.BooleanField()
    name = models.CharField(max_length=5)
    coordX = models.CharField(max_length=15)
    coordY = models.CharField(max_length=15)
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)
    viatura = models.ForeignKey(Viatura, on_delete=models.PROTECT)
    warehouse = models.OneToOneField(Warehouse, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class ModeloEquipamento(models.Model):
    active = models.BooleanField()
    name = models.CharField(max_length=80)    

    def __str__(self):
        return self.name


class Equipamento(models.Model):
    active = models.BooleanField()
    serial = models.CharField(max_length=80, unique=True)    
    assetnumber1 = models.CharField(max_length=80, unique=True)
    assetnumber2 = models.CharField(max_length=80, unique=True, null=True)
    modeloequipamento = models.ForeignKey(ModeloEquipamento, on_delete=models.PROTECT)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.PROTECT)

    def __str__(self):
        return self.assetnumber1

class Posto(models.Model):
    active = models.BooleanField()
    name = models.CharField(max_length=60)
    cgmp = models.CharField(max_length=5)
    status_opc = models.BooleanField()
    status_vip = models.BooleanField()
    coordX = models.CharField(max_length=15)
    coordY = models.CharField(max_length=15)
    classe = models.ForeignKey(Classe, on_delete=models.PROTECT)
    base = models.ForeignKey(Base, on_delete=models.PROTECT)
    warehouse = models.OneToOneField(Warehouse, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class TipoEvento(models.Model):
    active = models.BooleanField()
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Evento(models.Model):
    active = models.BooleanField()
    data_planejado = models.PositiveIntegerField()
    data_realizado = models.PositiveIntegerField()
    number = models.CharField(max_length=15)
    resumo = models.TextField(null=True)
    posto = models.ForeignKey(Posto, on_delete=models.PROTECT)
    base = models.ForeignKey(Base, on_delete=models.PROTECT)
    form = models.ForeignKey(Form, on_delete=models.PROTECT)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)

    def __str__(self):
        return self.number


class Punch(models.Model):
    active = models.BooleanField()
    timestamp = models.PositiveIntegerField()
    tipo = models.BooleanField()
    coordX = models.CharField(max_length=15)
    coordY = models.CharField(max_length=15)
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)

    def __str__(self):
        return self.tipo

