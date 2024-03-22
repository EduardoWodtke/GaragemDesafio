from django.contrib import admin

from .models import Categoria
from .models import Marca
from .models import Modelo
from .models import Cor
from .models import Acessorio


admin.site.register(Categoria)
admin.site.register(Marca)
admin.site.register(Modelo)
admin.site.register(Cor)
admin.site.register(Acessorio)
