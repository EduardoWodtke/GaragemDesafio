from django.contrib import admin

from .models import Categoria
from .models import Marca
from .models import Modelo


admin.site.register(Categoria)
admin.site.register(Marca)
admin.site.register(Modelo)