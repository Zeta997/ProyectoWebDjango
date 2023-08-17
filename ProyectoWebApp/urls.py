from django.urls import path
from ProyectoWebApp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.Home, name="home"),
    path('tienda/', views.Tienda,name="tienda"),
    path('blog/', views.Blog, name="blog"),
    path('contacto/', views.Contacto, name="contacto"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)