# -*- coding: utf-8 -*-

from django.conf.urls import url
from sistema.modelviews.animals import AnimalListView, AnimalCreateView, AnimalUpdateView, AnimalDeleteView
from sistema.modelviews.procedimentos import ProcedimentoListView, ProcedimentoCreateView, ProcedimentoUpdateView, \
    ProcedimentoDeleteView
from sistema.modelviews.usuario import UsuarioListView, UsuarioCreateView, UsuarioUpdateView, UsuarioDeleteView
from sistema.views import HomeView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='sistema_home'),
    url(r'^animals/$', AnimalListView.as_view(), name='sistema_animals_list'),
    url(r'^animals/create/$', AnimalCreateView.as_view(), name='sistema_animals_create'),
    url(r'^animals/(?P<pk>[0-9]+)/update/$', AnimalUpdateView.as_view(), name='sistema_animals_update'),
    url(r'^animals/(?P<pk>[0-9]+)/delete/$', AnimalDeleteView.as_view(), name='sistema_animals_delete'),
    url(r'^usuario/$', UsuarioListView.as_view(), name='sistema_usuario_list'),
    url(r'^usuario/create/$', UsuarioCreateView.as_view(), name='sistema_usuario_create'),
    url(r'^usuario/(?P<pk>[0-9]+)/update/$', UsuarioUpdateView.as_view(), name='sistema_usuario_update'),
    url(r'^usuario/(?P<pk>[0-9]+)/delete/$', UsuarioDeleteView.as_view(), name='sistema_usuario_delete'),
    url(r'^procedimento/$', ProcedimentoListView.as_view(), name='sistema_procedimento_list'),
    url(r'^procedimento/create/$', ProcedimentoCreateView.as_view(), name='sistema_procedimento_create'),
    url(r'^procedimento/(?P<pk>[0-9]+)/update/$', ProcedimentoUpdateView.as_view(), name='sistema_procedimento_update'),
    url(r'^procedimento/(?P<pk>[0-9]+)/delete/$', ProcedimentoDeleteView.as_view(), name='sistema_procedimento_delete'),
]
