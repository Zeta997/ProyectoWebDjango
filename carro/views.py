from django.shortcuts import render, redirect
from carro.carro import Carro
from tienda.models import Producto
# Create your views here.

def agregarProducto(request,producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id =producto_id)

    carro.agregarProducto(producto)
    return redirect('tienda')

def eliminarProducto(request,producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id =producto_id)

    carro.eliminarProducto(producto=producto)
    return redirect('tienda')

def quitarProducto(request,producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id =producto_id)

    carro.quitarProducto(producto=producto)
    return redirect('tienda')

def limpiarCarro(request, producto_id):
    carro =Carro(request)

    carro.limpiarCarro()

    return redirect('tienda')