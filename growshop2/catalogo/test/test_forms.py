from django.test import TestCase
from catalogo.forms import CategoriaForm, MarcaForm, TipoForm
from catalogo.models import Categoria, Marca, Tipo

class CategoriaFormTest(TestCase):
    def test_valid_form(self):
        categor = Categoria.objects.create(catego='Kits1')
        categor.save()
        cate = Categoria.objects.get(id=1)
       
        data = {'id':cate.id, 'catego':cate.catego}
        form = CategoriaForm(data)
        print(form.errors)
        self.assertTrue(form.is_valid())

class MarcaFormTest(TestCase):
    def test_valid_form(self):
        marc = Marca.objects.create(id='c3d3bf25-0869-4c51-9e76-9c54d089da33' ,nombreMar='CALVOGLASS')
        marc.save()
        mar = Marca.objects.first()

        data = {'id':mar.id, 'nombreMar':mar.nombreMar}
        form = MarcaForm(data)
        print(form.errors)
        self.assertTrue(form.is_valid())

class TipoFormTest(TestCase):
    def test_valid_form(self):
        tip = Tipo.objects.create(nombreEnt='Humor1')
        tip.save()
        ti = Tipo.objects.get(id=1)
       
        data = {'id':ti.id, 'nombreEnt':ti.nombreEnt}
        form = TipoForm(data)
        print(form.errors)
        self.assertTrue(form.is_valid())