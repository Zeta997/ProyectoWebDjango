from django import forms

class Formulario(forms.Form):
   
    titulo = forms.CharField(required=True)
    nombre= forms.CharField(required=True)
    email = forms.EmailField(required=True)
    contenido = forms.CharField(widget=forms.Textarea)
