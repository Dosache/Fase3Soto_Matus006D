from django import forms
from . models import Categoria, Marca, Accesorio, Tipo

class CategoriaForm(forms.ModelForm):
    catego = forms.CharField(label='Categoria',max_length=200, widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    
    class Meta:
        model = Categoria
        fields = ('catego',)

class MarcaForm(forms.ModelForm):
    nombreMar = forms.CharField(label='Nombre',max_length=100, widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))

    class Meta:
        model = Marca
        fields = ('nombreMar',)

class TipoForm(forms.ModelForm):
    nombreEnt = forms.CharField(label='Nombre',max_length=100, widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))

    class Meta:
        model = Tipo
        fields = ('nombreEnt',)

class AccesorioForm(forms.ModelForm):
    nombre = forms.CharField(label='Nombre',max_length=200, widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    marca = forms.CharField(label='Marca', max_length=50, widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    precio = forms.CharField(label='Precio', max_length=50, widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    resumen = forms.CharField(label='Resumen', max_length=1000, widget=forms.Textarea(
        attrs={
            'class':'form-control'
        }
    ))
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), label='Categoria',
            widget=forms.Select(
            attrs={
                'class':'form-control' 
            }
            ))
    class Meta:
        model = Accesorio
        fields = ('nombre', 'marca', 'precio', 'resumen', 'categoria',)