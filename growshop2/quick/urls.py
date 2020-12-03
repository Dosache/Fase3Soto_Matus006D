from django.urls import include, path
from . import views
from django.views.generic.base import TemplateView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

app_name='quick'

urlpatterns = [
    path('', include(router.urls)),
    path('rest-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
]
#TemplateView.as_view(template_name='home.html'), name='home'
#path('agregar/', views.UserViewSet.as_view(), name='agregar'),
#path('agregar/', include(router.register('users', views.UserViewSet))),
#