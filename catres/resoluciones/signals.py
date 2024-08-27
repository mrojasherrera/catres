from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.postgres.search import SearchVector
from .models import Resoluciones

@receiver(post_save, sender=Resoluciones)
def update_search_vector(sender, instance, created, **kwargs):
    # Este código se ejecuta tanto en insert como en update
    search_vector = (
        SearchVector('numero', weight='A') +
        SearchVector('sumario', weight='B') +
        SearchVector('observaciones', weight='C')
    )

    # Lógica adicional si el objeto fue recién creado
    if created:
        print("Registro insertado")
    
    # Actualiza el campo `tsbuscar` en la base de datos
    Resoluciones.objects.filter(pk=instance.pk).update(tsbuscar=search_vector)
