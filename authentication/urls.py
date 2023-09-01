from django.urls import path
from authentication.views import VRegistration, cerrar_sesion, log

urlpatterns= [
    path('', VRegistration.as_view(), name='Authentication'),
    path('cerrar_sesion', cerrar_sesion, name='logout'),
    path('log', log , name='login'),
]