from django.shortcuts import render

# Create your views here.
def listaproducto(request):
    return render(request,"lista_producto.html")

def detalleproducto(request):
    return render(request,"detalle_producto.html")