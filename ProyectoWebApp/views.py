from django.shortcuts import render

# Create your views here.
def BasePage(request):
    return render(request, "base.html")