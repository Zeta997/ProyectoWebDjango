from django.contrib import admin
from .models import CategoriaProducto, Producto
# Register your models here.

# Con este archivo podemos personalizar la visualizacion de los elementos que queremos mostrar en el aparto admin
class CategoriaAdmin(admin.ModelAdmin):
    list_display=('nombre',)
    readonly_fields=('create','update')

class ProductoAdmin(admin.ModelAdmin):
    list_display=('nombre', 'precio', 'disponibilidad')
    readonly_fields=('create', 'update')

admin.site.register( CategoriaProducto, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)