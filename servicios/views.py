from django.shortcuts import render
from servicios.models import Servicio as serviceElement
# Create your views here.

def Servicio(request):
    servicio = serviceElement.objects.all()
    return render(request, "servicios/services.html", {'servicio':servicio})