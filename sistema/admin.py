# -*- coding: utf-8 -*-

from django.contrib import admin
from sistema.models import Usuario, Animal, Procedimento


class AnimalAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'idade', 'raca')


class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipos', 'email', 'telefone')


class ProcedimentoAdmin(admin.ModelAdmin):
    list_display = ('data', 'nome', 'custo', 'animal', 'usuario')


admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Animal, AnimalAdmin)
admin.site.register(Procedimento, ProcedimentoAdmin)

