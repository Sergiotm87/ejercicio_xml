# -*- coding: utf-8 -*-
from lxml import etree
#
#Introduce el apellido de una casa y muestra todos los miembros de esa familia que hayan participado en alguna batalla
#
doc = etree.parse('batallasjuegotronos.xml')
raiz=doc.getroot()


casa=raw_input("Introduce el nombre de una casa: ")

listamiembros=[]

#recorremos el xml tomando los elementos que contienen el nombre de la casa(apellido)
#encontramos elementos compuestos por varios nombres o un texto que los contiene,
#los separamos dentro de una lista y tomamos el que corresponda

for elem in raiz.getiterator():
    try:
        if casa in elem.text:
            if elem.text.count(' ') >0:
                split=elem.text.split(',')
                miembro = [s for s in split if casa in s]
                if miembro[0].count(' ') <3:
                    listamiembros.append(miembro[0].lstrip())
    except TypeError:
        pass

listamiembros2= list(set(listamiembros))

print "\nMiembros de la casa",casa,":"
for elem in listamiembros2:
    print elem