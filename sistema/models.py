# -*- coding: utf-8 -*-

from django.db import models


class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Animal(TimeStamp):
    TIPOS = (("cachorro", u"Cachorro"), ("gato", u"Gato"), ("passaro", u"Pássaro"))
    nome = models.CharField(max_length=50)
    idade = models.IntegerField()
    raca = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50, choices=TIPOS)

    def agir(self):
        if self.tipo == self.TIPOS[0][0]:
            print "woof woof"
        elif self.tipo == self.TIPOS[1][0]:
            print "meow"
        elif self.tipo == self.TIPOS[2][0]:
            print "piu piu"
        else:
            print "sou um animal misterioso"

    def __unicode__(self):
        return u"%s, %s" % (self.nome, self.tipo)


class Usuario(TimeStamp):
    TIPOS_USUARIOS = (("cliente", u"Cliente"), ("medico", u"Médico"), ("funcionario", u"Funcionário"))
    nome = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    telefone = models.CharField(max_length=50)
    tipos = models.CharField(max_length=50, choices=TIPOS_USUARIOS)
    animal = models.ForeignKey(Animal, null=True, blank=True)

    def __unicode__(self):
        return u"%s, %s" % (self.nome, self.tipos)


class Procedimento(TimeStamp):
    NOMES = (("banho", u"Banho"), ("cirurgia", u"Cirurgia"), ("consulta", u"Consulta"))
    data = models.DateTimeField()
    nome = models.CharField(max_length=50, choices=NOMES)
    custo = models.DecimalField(max_digits=8, decimal_places=2)
    animal = models.ForeignKey(Animal)
    usuario = models.ForeignKey(Usuario)

    def __unicode__(self):
        return u"%s, %s" % (self.nome, self.animal)
