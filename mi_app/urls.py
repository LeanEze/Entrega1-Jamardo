from django.contrib import admin
from django.urls import path
from mi_app import views
from mi_app.views import busqueda_formularios, mostrar_inicio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', mostrar_inicio),
    path('cerdos/', views.cerdo_formulario, name='cerdos'),
    path('gatos/', views.gato_formulario, name='gatos'),
    path('perros/', views.perro_formulario, name='perros'),
    path('buscarFormularios/',views.busqueda_formularios, name='BuscarFormularios'),
    path('buscar/', views.buscar),

    ]
   
