from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . models import Categoria, Accesorio, InstanciaAccesorio, Marca

# Create your views here.
def inicio(request): #Request = consulta HTTP
    num_catego=Categoria.objects.all()#.count()
    
    return render( #Crea y retorna una página HTML como respuesta
        request,
        'inicio.html',
        context={'num_catego':num_catego},
    )

def proximamente(request): #Request = consulta HTTP
    num_catego=Categoria.objects.all()#.count()
    
    return render( #Crea y retorna una página HTML como respuesta
        request,
        'proximamente.html',
        context={'num_catego':num_catego},
    )

def autocultivo(request): #Request = consulta HTTP
    num_catego=Categoria.objects.all()#.count()
    
    return render( #Crea y retorna una página HTML como respuesta
        request,
        'autocultivo.html',
        context={'num_catego':num_catego},
    )

def quienes(request): #Request = consulta HTTP
    num_catego=Categoria.objects.all()#.count()
    
    return render( #Crea y retorna una página HTML como respuesta
        request,
        'quienes.html',
        context={'num_catego':num_catego},
    )

def registro(request): #Request = consulta HTTP
    num_catego=Categoria.objects.all()#.count()
    
    return render( #Crea y retorna una página HTML como respuesta
        request,
        'registro.html',
        context={'num_catego':num_catego},
    )

def cepa1(request): #Request = consulta HTTP
    num_catego=Categoria.objects.all()#.count()
    
    return render( #Crea y retorna una página HTML como respuesta
        request,
        'cepa1.html',
        context={'num_catego':num_catego},
    )

def seta1(request): #Request = consulta HTTP
    num_catego=Categoria.objects.all()#.count()
    
    return render( #Crea y retorna una página HTML como respuesta
        request,
        'seta1.html',
        context={'num_catego':num_catego},
    )

def terminosycon(request): #Request = consulta HTTP
    num_catego=Categoria.objects.all()#.count()
    
    return render( #Crea y retorna una página HTML como respuesta
        request,
        'terminosycon.html',
        context={'num_catego':num_catego},
    )

class AccesorioCreate(CreateView):
    model = Accesorio
    fields = '__all__'

class AccesorioUpdate(UpdateView):
    model = Accesorio
    fields = '__all__'
    
class AccesorioDelete(DeleteView):
    model = Accesorio
    success_url = reverse_lazy('Accesorios')

class AccesorioDetailView(generic.DetailView):
    model = Accesorio 

