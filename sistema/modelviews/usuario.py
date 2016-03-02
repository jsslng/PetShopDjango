# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from sistema.models import Usuario


class UsuarioMixin(object):
    model = Usuario


class UsuarioListView(UsuarioMixin, ListView):
    pass


class UsuarioCreateView(UsuarioMixin, CreateView):
    fields = ('nome', 'email', 'telefone', 'tipos')

    def get_success_url(self):
        return reverse('sistema_usuario_list')


class UsuarioUpdateView(UsuarioMixin, UpdateView):
    fields = ('nome',)
    template_name = 'sistema/usuario_update.html'

    def get_success_url(self):
        return reverse('sistema_usuario_list')


class UsuarioDeleteView(UsuarioMixin, DeleteView):
    def get_success_url(self):
        return reverse('sistema_usuario_list')