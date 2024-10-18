from django.urls import path
from . import views

app_name= 'tienda' 
urlpatterns = [
    path('listaproducto/', views.listaproducto,name="listaproducto"),
    path('detalleproducto/', views.detalleproducto,name="detalleproducto"),

]