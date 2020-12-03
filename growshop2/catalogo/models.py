from django.db import models			
from django.urls import reverse  		#redirecciona una url de un libro al browser 
import uuid  							#se utiliza para definir atributos clave (pk)

# Create your models here.
class Categoria(models.Model):
	catego = models.CharField(max_length=200)
	
	def __str__(self):
		return self.catego

class Marca(models.Model):
	nombreMar = models.CharField(max_length=100)
	id = models.UUIDField(primary_key=True, default=uuid.uuid4)
	class Meta:
		ordering = ['nombreMar']

	def __str__(self):
		return f'{self.nombreMar}'	

class Accesorio(models.Model):
    
	nombre = models.CharField(max_length=200)
	marca = models.ForeignKey('Marca', on_delete=models.SET_NULL, null=True)
	precio = models.IntegerField(blank=True)
	imagen = models.ImageField(upload_to='imagen/', null=False)
	resumen = models.TextField(max_length=1000)
	categoria = models.ManyToManyField(Categoria)
    
	def get_absolute_url(self):
		return reverse('accesorio-detail', args=[str(self.id)])

	def __str__(self):
		return '{} | Categoria: {} | Precio: {}'.format(self.nombre, self.marca, self.precio) #return self.nombre,self.marca,self.precio
#CREACION DE ENTRADAS------------------------------------------------------------------------------
class Tipo(models.Model):
	nombreEnt = models.CharField(max_length=100)

	def __str__(self):
		return self.nombreEnt

class Entrada(models.Model):
    
	titulo = models.CharField(max_length=100)
	descripcion = models.TextField(max_length=5000)
	imagen = models.ImageField(upload_to='imagen/', null=False)
	tipoentrada = models.ManyToManyField(Tipo)
    
	def get_absolute_url(self):
		return reverse('entrada-detail', args=[str(self.id)])

	def __str__(self):
		return '{} | Tipo de entrada: {} |'.format(self.titulo, self.tipoentrada)
#CREACION DE ENTRADAS------------------------------------------------------------------------------




class InstanciaAccesorio(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4)
	accesorio = models.ForeignKey('Accesorio', on_delete=models.SET_NULL, null=True)
	imprint = models.CharField(max_length=200)
	devolver = models.DateField(null=True, blank=True)

	LOAN_STATUS = (
		('m', 'En mantención'),
		('o', 'En préstamo'),
		('a', 'Disponible'),
		('r', 'Reservado'),
	)

	status = models.CharField(
		max_length=1,
		choices=LOAN_STATUS,
		blank=True,
		default='m',
		help_text='Disponibilidad del producto',
	)

	class Meta:
		ordering = ['devolver']

	def __str__(self):
		return f'{self.id} , ({self.accesorio.nombre})'

