from django.db import models

# Create your models here.
from tienda.models import Producto
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import F, Sum, FloatField
# Create your models here.

user=get_user_model()

class Pedido(models.Model):

    userActive= models.ForeignKey(user, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id
    
    @property 
    def total(self):
        return self.LineaPedido_set.aggregate(
            total = Sum(F('precio')*F('cantidad'), output_field= FloatField())
        )['total']

    class Meta:
        verbose_name='pedido'
        verbose_name_plural='pedidos'
        ordering=['id']

class LineaPedido(models.Model):
    userActive= models.ForeignKey(user, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.producto.nombre} {self.cantidad}'

    class Meta:
        verbose_name='LineaPedido'
        verbose_name_plural='LineasPedidos'
        ordering=['id']