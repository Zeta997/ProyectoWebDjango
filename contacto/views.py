from django.shortcuts import render, redirect
from .forms import Formulario
from ProyectoWeb import settings
from django.core.mail import send_mail, EmailMessage
from django.http import HttpResponse
# Create your views here.

def Contacto(request):

    if request.method=='POST':
        emailContact= settings.EMAIL_HOST_USER
        contactForm = Formulario(request.POST)
        if contactForm.is_valid:
            titulo= request.POST.get('titulo')
            nombre= request.POST.get('nombre')
            contenido= request.POST.get('contenido')
            email=request.POST.get('email')
            
            email = EmailMessage(f'Asunto: {titulo}',
            f'El usuario {nombre} con correo {email} escribe: \n \n {contenido}',
            '', 
            [f'{emailContact}'],
            reply_to=[email])
            try:
                email.send()
                return redirect('/contacto/?valido')
            except:
                return redirect('/contacto/?invalido')
            
            
    else:
        contactForm = Formulario()
    return render(request, 'contacto_django.html',{'contactForm':contactForm})