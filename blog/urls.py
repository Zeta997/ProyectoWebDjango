from django.urls import path
from blog import views

urlpatterns =[
    path('', views.Blog, name='blog'),
    path('categoria/<categoria_id>/', views.Categorias, name='categoria'),
]