from django.contrib import admin
from django.urls import path
from mi_app import views
from mi_app.views import datos_cerdos, mostrar_inicio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', mostrar_inicio),
    path('cerdos/', datos_cerdos),
    path('gatos/', views.gato_formulario, name='gatos'),
    path('perros/', views.perro_formulario, name='perros'),
    
    ]
   
