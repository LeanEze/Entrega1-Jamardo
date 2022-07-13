from django.contrib import admin
from django.urls import path
from mi_app.views import datos_cerdos, datos_gatos, datos_perros 

urlpatterns = [
    path('cerdos/', datos_cerdos),
    path('gatos/', datos_gatos),
    path('perros/', datos_perros),
    ]
   