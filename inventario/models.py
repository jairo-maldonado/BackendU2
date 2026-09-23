from django.db import models

class Producto(models.Model):
    nombre      = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    precio      = models.PositiveIntegerField()
    stock       = models.PositiveIntegerField()
    activo      = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre 