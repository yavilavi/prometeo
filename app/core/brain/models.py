from django.db import models
from datetime import datetime


class Position(models.Model):
    position_name = models.CharField(max_length=50, unique=True, verbose_name='Nombre del cargo')
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.position_name

    class Meta:
        verbose_name = 'Position'
        verbose_name_plural = 'Positions'
        ordering = ['id']


class Lob(models.Model):
    lob_name = models.CharField(max_length=150, unique=True, verbose_name='Nombre campaña')
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.lob_name

    class Meta:
        verbose_name = 'Lob'
        verbose_name_plural = "Lob's"
        ordering = ['id']


class Agents(models.Model):
    document_number = models.CharField(max_length=30, null=False, blank=False, unique=True, verbose_name='Cédula')
    first_name = models.CharField(max_length=30, null=False, blank=False, verbose_name='Primer nombre')
    middle_name = models.CharField(max_length=30, null=True, blank=True, verbose_name='Segundo nombre')
    first_last_name = models.CharField(max_length=30, null=False, blank=False, verbose_name='Primer apellido')
    second_last_name = models.CharField(max_length=30, null=True, blank=True, verbose_name='Segundo apellido')
    gender = models.CharField(max_length=15, null=False, blank=False, verbose_name='Género')
    birth_date = models.DateField(default=datetime.now, verbose_name='Fecha de nacimiento')
    avaya_login = models.CharField(max_length=7, null=False, blank=False, verbose_name='Login de avaya')
    ccms_id = models.CharField(max_length=10, null=True, blank=True, verbose_name='Número de ccms')
    slack_id = models.CharField(max_length=20, null=False, blank=False, verbose_name='id de usuario en slack')
    dtvpan_user = models.CharField(max_length=50, null=True, blank=False, verbose_name='Usuario dtvpan')
    manager = models.ForeignKey('self',null=True, blank=True, on_delete=models.PROTECT, verbose_name='Jefe inmediato')
    position = models.ForeignKey(Position, on_delete=models.PROTECT, verbose_name='Cargo del empleado')
    lob = models.ForeignKey(Lob, on_delete=models.PROTECT)
    profile_picture = models.ImageField(upload_to='img/profile_pictures/%Y/%m/%d')
    status = models.BooleanField(default=True, verbose_name='Estado')
    date_hired = models.DateField(default=datetime.now, verbose_name='Fecha de contratación')
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.document_number

    class Meta:
        verbose_name = 'Agente'
        verbose_name_plural = 'Agentes'
        ordering = ['id']
