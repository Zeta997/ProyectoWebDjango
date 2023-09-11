from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
# Create your views here.

class VRegistration(View):

    def get(self, request):
        form = UserCreationForm()
        return render(request, 'registro.html', {'form':form})

    def post(self, request):
        form = UserCreationForm(request.POST)

        try:
            usuario = form.save() #se almacena los dato del usuario automaticamente en la BBDD
            login(request, usuario)
            return redirect('/')
        except Exception as e:
            print(e)
            # for msg in form.error_messages:
            #     messages.error(request, form.error_messages[msg])
            return render(request, 'registro.html', {'form':form})

def cerrar_sesion(request):
    logout(request)
    return redirect('/')

def log(request):
    
    if request.method=='POST':
        form = AuthenticationForm(request, data=request.POST) 
        if form.is_valid():
            nombreUser= form.cleaned_data['username']
            passwordUser = form.cleaned_data['password']
            user = authenticate(username=nombreUser, password= passwordUser)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, 'Usuario no valido.')
        else :
            messages.error(request, 'Informacion incorrecta.')
    form = AuthenticationForm()
    return render(request, 'log.html',{'form':form})

