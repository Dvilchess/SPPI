from django.db import models

class Coordenada(models.Model):
    latitud = models.FloatField()  # Campo para latitud
    longitud = models.FloatField()  # Campo para longitud

    def __str__(self):
        return f"Coordenadas: {self.latitud}, {self.longitud}"

from core.models import Coordenada
print(Coordenada.objects.all())
