from django.db import models
from datetime import datetime


class Position(models.Model):

    position_name = models.CharField(max_length=60, unique=True, verbose_name='Cargo', default='Agent')
    created_at = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.position_name

    class Meta:
        verbose_name = 'Position'
        verbose_name_plural = 'Positions'
        ordering = ['id']


class Employee(models.Model):
    document_number = models.CharField(max_length=20, unique=True, verbose_name='Cédula')
    first_name = models.CharField(max_length=150, verbose_name='Nombres')
    last_name = models.CharField(max_length=150, verbose_name='Apellidos')
    login = models.CharField(max_length=7, unique=True, verbose_name='login')
    LOB = models.PositiveIntegerField(verbose_name='LOB id')
    slack_id = models.CharField(max_length=20, unique=True, verbose_name='Id usuario slack')
    ccms_id = models.CharField(max_length=10, null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars', null=True, blank=True)
    gender = models.CharField(max_length=1, verbose_name='Sexo')
    state = models.BooleanField(default=True)
    employee_since = models.DateField(default=datetime.now, verbose_name='Fecha contratación')
    created_at = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=True)

    position = models.ForeignKey(Position, on_delete=models.PROTECT)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
        ordering = ['id']
