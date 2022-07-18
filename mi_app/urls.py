from django.contrib import admin
from django.urls import path
from mi_app import views
from mi_app.views import mostrar_inicio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', mostrar_inicio),
    path('cerdos/', views.cerdo_formulario, name='cerdo'),
    path('gatos/', views.gato_formulario, name='gato'),
    path('perros/', views.perro_formulario, name='perro'),
    path('buscarFormularios/',views.buscar_nombre, name='BuscarFormularios'),
    path('resultadosBusqueda/', views.buscar, name='ResultadosBusqueda'),

    ]
   
