from django.contrib import admin

# Register your models here.

from . models import Categoria, Accesorio, InstanciaAccesorio, Marca

admin.site.register(Categoria)
admin.site.register(Accesorio)
admin.site.register(InstanciaAccesorio)
admin.site.register(Marca) 


