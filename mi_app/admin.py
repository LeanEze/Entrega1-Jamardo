from django.contrib import admin
from mi_app.models import perro
from mi_app.models import cerdo
from mi_app.models import gato


admin.site.register(perro)

admin.site.register(gato)

admin.site.register(cerdo)