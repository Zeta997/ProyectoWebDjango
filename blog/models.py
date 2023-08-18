from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'
    def __str__(self) -> str:
        return self.nombre

class Post(models.Model):
    imagen = models.ImageField(upload_to='post',null=True, blank=True)
    titulo= models.CharField(max_length=50)
    contenido= models.TextField(max_length=200)
    autor = models.ForeignKey(User,on_delete=models.CASCADE)
    categoria= models.ManyToManyField(Categoria)
    class Meta:
        verbose_name='post'
        verbose_name_plural='posts'