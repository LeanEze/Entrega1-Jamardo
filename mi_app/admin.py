from django.contrib import admin
from mi_app.models import Perro
from mi_app.models import Cerdo
from mi_app.models import Gato


admin.site.register(Perro)

admin.site.register(Gato)

admin.site.register(Cerdo)