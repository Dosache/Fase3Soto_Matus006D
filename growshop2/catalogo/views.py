from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . models import Categoria, Accesorio, InstanciaAccesorio, Marca, Tipo, Entrada

# Create your views here.
def inicio(request): #Request = consulta HTTP
    num_catego=Categoria.objects.all()#.count()
    
    return render( #Crea y retorna una página HTML como respuesta
        request,
        'inicio.html',
        context={'num_catego':num_catego},
    )

def proximamenteCategoria(request): #Request = consulta HTTP
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
    )

class AccesorioCreate(CreateView):
    model = Accesorio
    fields = '__all__'

class AccesorioUpdate(UpdateView):
    model = Accesorio
    fields = '__all__'
    
class AccesorioDelete(DeleteView):
    model = Accesorio
    success_url = reverse_lazy('inicio')

class AccesorioDetailView(generic.DetailView):
    model = Accesorio 

def proximamente(request):
    num_accesorio=Accesorio.objects.all() #objetos tipo accesorio
    
    return render(
        request,
        'proximamente.html',
        context={'num_accesorio':num_accesorio},
    )

#creacion de vistas/def

class EntradaCreate(CreateView):
    model = Entrada
    fields = '__all__'

class EntradaUpdate(UpdateView):
    model = Entrada
    fields = '__all__'
    
class EntradaDelete(DeleteView):
    model = Entrada
    success_url = reverse_lazy('inicio')

class EntradaDetailView(generic.DetailView):
    model = Entrada

class EntradaListView(generic.ListView): #for de entradas
    model = Entrada
    paginate_by = 10