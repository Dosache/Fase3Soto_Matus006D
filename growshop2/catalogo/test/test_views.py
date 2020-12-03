from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

from catalogo.models import Categoria, Marca, Accesorio, Entrada, Tipo

class CategoriasListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 13 authors for pagination tests
        number_of_categorias = 13
    
        for categoria_id in range(number_of_categorias):
            Categoria.objects.create(
                catego=f'Extracciones {categoria_id}',
            )
           
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/catalogo/tienda/')
        self.assertEqual(response.status_code, 200)

class MarcaListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_marca = 13
        
        for marca_id in range(number_of_marca):
            test_marca = Marca.objects.create(
                nombreMar=f'OCB {marca_id}',
            )
            test_marca.save()
    
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/catalogo/tienda/')
        self.assertEqual(response.status_code, 200)
           
class TipoListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 13 authors for pagination tests
        number_of_tipo = 13

        for tipo_id in range(number_of_tipo):
            Tipo.objects.create(
                nombreEnt=f'Informativo {tipo_id}',
            )
           
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/catalogo/entrada/')
        self.assertEqual(response.status_code, 200)

"""class AccesorioListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_accesorio = 13
        g = Categoria.objects.create(catego='Extracciones')
        with open('catalogo/static/img/ak.jpg', 'rb') as file:
            document = SimpleUploadedFile(file.name, file.read(), content_type='image/jpg')

        for accesorio_id in range(number_of_accesorio):
            test_accesorio = Accesorio.objects.create(
                nombre=f' {accesorio_id}',
                marca=f'OCB {accesorio_id}',
                precio=f'5000 {accesorio_id}',
                imagen=document,
                resumen=f'Prueba {accesorio_id}',
                categoria=g
            )
            
            test_accesorio.save()

           
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/catalogo/tienda/')
        self.assertEqual(response.status_code, 200)"""
           