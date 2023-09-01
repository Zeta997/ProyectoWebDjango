from django.urls import path
from carro import views
urlpatterns =[
    path('agregar/<int:producto_id>/', views.agregarProducto, name='agregar'),
    path('eliminar/<int:producto_id>/', views.eliminarProducto, name='eliminar'),
    path('restar/<int:producto_id>/', views.quitarProducto, name='restar'),
    path('limpiar/', views.limpiarCarro, name='limpiar'),

]