from django.db import models
from applications.departamento.models import Departamento




# Create your models here.
class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)

    def __str__(self):
        return self.habilidad


class Empleado(models.Model):
    JOB_CHOICES = (
        ('0', 'Contador'),
        ('1', 'Administrador'),
        ('2', 'Economista'),
        ('3', 'Otro'),
    )

    first_name = models.CharField('Nombres', max_length=60)
    last_name = models.CharField(max_length=60)
    job = models.CharField('Trabajo', max_length=50, choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    Habilidades = models.ManyToManyField(Habilidades)


    # image = models.ImageField('Imagen', upload_to=None, height_field=None, width_field=None, max_length=None)

    class Meta:
        verbose_name = 'Mi Empleado'
        verbose_name_plural = 'Empleados de la Empresa'
        ordering = ['-first_name', 'last_name']
        unique_together = ('first_name', 'last_name')

    def __str__(self):
        return str(self.id) + ', ' + self.first_name + ', ' + self.last_name