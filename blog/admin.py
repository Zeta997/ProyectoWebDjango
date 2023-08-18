from django.contrib import admin
from blog.models import Categoria, Post
# Register your models here.


class CategoriaAdmin(admin.ModelAdmin):
    list_display=("nombre",)
    readonly_fields=('create','update')

class PostAdmin(admin.ModelAdmin):
    list_display=("titulo", "contenido", "imagen", )

admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Post, PostAdmin)