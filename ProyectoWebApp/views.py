from django.shortcuts import render
# Create your views here.
def Home(request):
    return render(request, "home.html")

# def Servicio(request):
#     servicio = serviceElement.objects.all()
#     return render(request, "services.html", {'servicio':servicio})

def Contacto(request):
    return render(request, "contacto.html")

def Tienda(request):
    return render(request,"tienda.html")

def Blog(request):
    return render(request, "blog.html")