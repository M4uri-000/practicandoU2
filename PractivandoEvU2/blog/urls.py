from django.urls import path
from . import views

app_name="blog"
urlpatterns = [
    path('', views.articulos,name="blogs"),
    path('detalles/', views.detalles,name="detalles"),
    path('detalles_juego/', views.detalles_juegos,name="detalles_juegos"),
]