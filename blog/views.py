from django.shortcuts import render
from blog.models import Post
# Create your views here.
def Blog(request):
    posts= Post.objects.all()
    return render(request, 'blog.html', {'posts': posts})