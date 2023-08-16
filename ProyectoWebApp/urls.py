from django.urls import path
from ProyectoWebApp import views

urlpatterns = [
    path('', views.Home, name="home"),
    path('servicio/', views.Servicio, name="servicio"),
    path('tienda/', views.Tienda,name="tienda"),
    path('blog/', views.Blog, name="blog"),
    path('contacto/', views.Contacto, name="contacto"),
]