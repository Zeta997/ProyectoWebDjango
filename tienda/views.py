from django.shortcuts import render
from .models import Producto, CategoriaProducto


def Tienda(request):
    producto = Producto.objects.all()
    categoria= CategoriaProducto.objects.all()
    return render(request,'tienda/tienda.html', {'producto':producto})
