from django.shortcuts import render

# Create your views here.
def articulos(request):
    return render(request,"blog/lista_articulos.html")

def detalles(request):
    return render(request,"blog/detalle_articulos.html")

def detalles_juegos(request):
    return render(request,"blog/detalle_articulo_juegos.html") 