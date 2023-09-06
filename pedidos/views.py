from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from pedidos.models import Pedido, LineaPedido
from carro.carro import Carro
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
# Create your views here.

@login_required(login_url='auth/log')
def procesar_pedido(request):
    pedido = Pedido.objects.create(userActive=request.user)
    carro=Carro(request)
    lista_pedido=list()
    for key, value in carro.carro.items():
        lista_pedido.append(LineaPedido(

            producto_id= key,
            cantidad=value['cantidad'],
            userActive= request.user,
            pedido = pedido
        ))
    
    enviar_mail(
        pedido= pedido,
        lista_pedido=lista_pedido,
        nombreUser = request.user.username,
        emailUser= request.user.email,
    )
    LineaPedido.objects.bulk_create(lista_pedido)

    messages.success(request, 'Pedido creado correctamente.')

    return redirect('../tienda')


def enviar_mail(**kwargs):
    asunto='Gracias por realizar el pedido'
    mensaje=render_to_string('pedido.html', {
        'pedido': kwargs.get('pedido'),
        'lista_pedido': kwargs.get('lista_pedido'),
        'nombreUsuario':kwargs.get('nombreUser')
    })

    mensaje_texto = strip_tags(mensaje)
    from_email = 'companyTestingServices@gmail.com'
    to_email= kwargs.get('emailUser')

    send_mail(asunto, mensaje_texto, from_email, [to_email], fail_silently=False, html_message=mensaje)