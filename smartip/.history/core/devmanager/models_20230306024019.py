from django.db import models

# Create your models here.
class DevType(models.Model):
    dev_type = models.CharField(max_length=20, verbose_name='Tipos de Dispositivo')

    def __str__(self) -> str:
        return self.dev_type
    
    class Meta:
        verbose_name = 'Tipo de Dispositivo'
        verbose_name_plural = 'Tipos de Dispositivos'
        db_table = 'TipoDispositivo'
        ordering = ['id']
        

class Brand(models.Model):
    dev_type = models.ForeignKey(DevType)
    brand = models.CharField(max_length=20, verbose_name='Marca')

    def __str__(self) -> str:
        return self.brand
    
    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'
        db_table = 'MarcaDispositivo'
        ordering = ['id']

class Model(models.Model):
    dev_type = models.ForeignKey(Brand)
    brand = models.ForeignKey(Brand)
    model = models.CharField(max_length=20, verbose_name='Modelo')
    img = models.ImageField(upload_to='DevImages/%Y/%m/%d')

    def __str__(self) -> str:
        return self.model
    
    class Meta:
        verbose_name = 'Modelo'
        verbose_name_plural = 'Modelos'
        db_table = 'ModeloDispositivo'
        ordering = ['id']




