from django.shortcuts import render
# Create your views here.
def Home(request):
    return render(request, "home.html")

def Tienda(request):
    return render(request,"tienda.html")
