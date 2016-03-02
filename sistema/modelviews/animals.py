# -*- coding: utf-8 -*-


from django.core.urlresolvers import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from sistema.models import Animal


class AnimalMixin(object):
    model = Animal


class AnimalListView(AnimalMixin, ListView):
    pass


class AnimalCreateView(AnimalMixin, CreateView):
    fields = ('nome', 'idade', 'raca', 'tipo')

    def get_success_url(self):
        return reverse('sistema_animals_list')


class AnimalUpdateView(AnimalMixin, UpdateView):
    fields = ('nome',)
    template_name = 'sistema/animal_update.html'

    def get_success_url(self):
        return reverse('sistema_animals_list')


class AnimalDeleteView(AnimalMixin, DeleteView):
    def get_success_url(self):
        return reverse('sistema_animals_list')
