from django.db import models
from django.contrib.postgres.search import SearchVectorField

# Create your models here.

class Resoluciones(models.Model):
    class Origen(models.TextChoices):
        PROCURADOR = 'ptn', 'PTN'
        SUBPROCURADOR = 'sptn', 'SPTN'

    numero = models.IntegerField()
    sumario = models.TextField(max_length=1024)
    origen = models.CharField(
        max_length=4,
        choices= Origen.choices,
        default=Origen.PROCURADOR
    )
    fecha = models.DateField()
    fecha_publicacion = models.DateField()
    observaciones = models.TextField()
    link_resolucion =  models.TextField(max_length=100, null=True)
    tsbuscar = SearchVectorField(null=True, blank=True)

    class Meta:
        db_table = 'resoluciones'
        verbose_name = 'Resoluciones'
        verbose_name_plural = 'Resoluciones'

    

        def __str__(self):
            return f"Numero: {self.numero} - Sumario: {self.sumario} - Fecha: {self.fecha} - O# bservaciones: {self.observaciones} - LinkResolucion: {self.link_resolucion}"
        
