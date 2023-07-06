from django.db import models

class Disco(models.Model):
    nombre_disco=models.CharField(max_length=40)
    ventas=models.IntegerField()
    artista = models.CharField(max_length=140, default='')
    genero= models.CharField(max_length=140, default='')
    def __str__(self):
        return self.nombre_disco

    
# Create your models here.
