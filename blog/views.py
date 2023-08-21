from django.shortcuts import render
from blog.models import Post, Categoria
# Create your views here.
def Blog(request):
    posts= Post.objects.all()
    category = Categoria.objects.all()
    return render(request, 'blog.html', {'posts': posts, 'category':category})

def Categorias(request,categoria_id):
    categoria=Categoria.objects.get(id=categoria_id)
    posts = Post.objects.filter(categoria=categoria)
    return render(request, 'categorias.html', {'categoria':categoria, 'posts':posts})
