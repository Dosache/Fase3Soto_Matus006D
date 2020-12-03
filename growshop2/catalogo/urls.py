from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('tienda/', views.proximamente, name ='proximamente'),
    path('autocultivo/', views.autocultivo, name='autocultivo'),
    path('quienes/', views.quienes, name='quienes'),
    path('registro/', views.registro, name='registro'),
    path('cepa1/', views.cepa1, name='cepa1'),
    path('seta1/', views.seta1, name='seta1'),
    path('terminosycon/', views.terminosycon, name='terminosycon'),
    path('accesorio/<int:pk>', views.AccesorioDetailView.as_view(), name='accesorio-detail'), #<str:pk>
    path('entrada/<int:pk>', views.EntradaDetailView.as_view(), name='entrada-detail'),
    path('entrada/', views.EntradaListView.as_view(), name='entrada'),
]

urlpatterns += [
    path('accesorio/crear/', views.AccesorioCreate.as_view(), name='accesorio_form'),
    path('accesorio/<int:pk>/actualizar/', views.AccesorioUpdate.as_view(), name='accesorio_update'),
    path('accesorio/<int:pk>/eliminar/', views.AccesorioDelete.as_view(), name='accesorio_delete'),
    path('entrada/crear/', views.EntradaCreate.as_view(), name='entrada_form'),
    path('entrada/<int:pk>/actualizar/', views.EntradaUpdate.as_view(), name='entrada_update'),
    path('entrada/<int:pk>/eliminar/', views.EntradaDelete.as_view(), name='entrada_delete'),
]
