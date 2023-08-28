from django.db import models

# Create your models here.

class CategoriaProducto(models.Model):
    nombre = models.CharField(max_length=50)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)

    class Meta: #define el nombre de la categoria tanto en singular como en plural
        verbose_name = 'categoriaProducto'
        verbose_name_plural= 'categoriasProducto'
    def __str__(self) -> str:
        return self.nombre

class Producto(models.Model):
    imagen = models.ImageField(upload_to='producto', blank=False, null=False)
    nombre = models.CharField(max_length=50)
    precio = models.FloatField()
    categoria = models.ForeignKey(CategoriaProducto, on_delete=models.CASCADE)
    disponibilidad = models.BooleanField(default=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'producto'
        verbose_name_plural='productos'
    
    def __str__(self):
       
        return '{} {} {}'.format(self.nombre, self.precio, self.disponibilidad)
    