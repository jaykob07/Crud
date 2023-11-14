from typing import Any
from django.db import models

# Create your models here.
class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo =  models.CharField(max_length=100, verbose_name='Titulo')
    image = models.ImageField(upload_to='imagenes', verbose_name='imagen', null=True)
    upload = models.FileField(upload_to='archivos_pdf')
    description = models.TextField(verbose_name='descripcion', null=True)
    

    def __str__(self):
        fila = "Titulo: " + self.titulo + " - " + "Descripcion: " + self.description
        return fila
    
    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()


