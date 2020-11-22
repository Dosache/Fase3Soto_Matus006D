from django.test import TestCase
from catalogo.models import Accesorio

class AccesoriosTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Accesorio.objects.create(nombre='PMG - Konjurer')

    def test_nombre(self):
        accesorio=Accesorio.objects.get(id=1)
        field_label= accesorio._meta.get_field('nombre').verbose_name
        self.assertEquals(field_label, 'nombre')

    def test_categoria(self):
        accesorio=Accesorio.objects.get(id=1)
        field_label = accesorio._meta.get_field('categoria').verbose_name
        self.assertEquals(field_label, 'Kits')
    
    def test_get_absolute_url(self):
        accesorio=Accesorio.objects.get(id=1)
        self.assertEquals(accesorio.get_absolute_url(), '/catalogo/accesorio/1')
     
    
