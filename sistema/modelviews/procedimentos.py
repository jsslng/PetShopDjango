# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from sistema.models import Procedimento


class ProcedimentoMixin(object):
    model = Procedimento


class ProcedimentoListView(ProcedimentoMixin, ListView):
    pass


class ProcedimentoCreateView(ProcedimentoMixin, CreateView):
    fields = ('data', 'nome', 'custo', 'animal', 'usuario')

    def get_success_url(self):
        return reverse('sistema_procedimento_list')


class ProcedimentoUpdateView(ProcedimentoMixin, UpdateView):
    fields = ('nome',)
    template_name = 'sistema/procedimento_update.html'

    def get_success_url(self):
        return reverse('sistema_procedimento_list')


class ProcedimentoDeleteView(ProcedimentoMixin, DeleteView):
    def get_success_url(self):
        return reverse('sistema_procedimento_list')