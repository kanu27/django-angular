from django.db import models

# Create your models here.
    
class Empresa(models.Model):
    nombre = models.CharField(max_length=250)
    webSite = models.URLField(max_length=200)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre
    
class Edificacion(models.Model):
    direccion = models.CharField(max_length=250)
    pais = models.CharField(max_length=250)
    descripcion = models.CharField(max_length=250)
    imagen = models.CharField(max_length=900)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    empresa = models.ForeignKey(Empresa,on_delete=models.CASCADE,related_name="edificacionlist")
    
    def __str__(self):
        return self.direccion