from django.shortcuts import render
from .models import Producto, CategoriaProducto

# Create your views here.

def Tienda(request):

    producto = Producto.objects.all()
    categoria= CategoriaProducto.objects.all()
    return render(request,'tienda/tienda.html', {'producto':producto})