from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import stripe
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
    imagen = models.ImageField(upload_to='producto', blank=True, null=True)
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

stripe.api_key = 'sk_test_51NmvPOL6EpuUZLgWxfSk5KC3FTyjyFZu68kTq8MDBrMbRwDbLjmkYhyLl6Dzm8zusjaJ4gtciKmV8VX3d9EQBCLk00HEKpZqQL'   
        
@receiver(post_save, sender=Producto)
def CrearArticuloStripe(sender, instance,**kwargs): 
    item_product=stripe.Product.create(
        name=f'{instance.nombre}',
        description = f'{instance.categoria}',
    )
    item_price=stripe.Price.create(
        unit_amount= int(instance.precio*100),
        currency = 'eur',
        product = item_product['id']
    )              

        