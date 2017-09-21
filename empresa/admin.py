from django.contrib import admin
from .models import Garagem, Onibus, Rota, Funcao, Funcionario, Viagem

admin.site.register(Garagem)
admin.site.register(Onibus)
admin.site.register(Rota)
admin.site.register(Funcao)
admin.site.register(Funcionario)
admin.site.register(Viagem)

# Register your models here.
