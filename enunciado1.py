# -*- coding: utf-8 -*-
from lxml import etree
#
#    Muestra todas las batallas ordenadas por la region en la que se produjeron
#
doc = etree.parse('batallasjuegotronos.xml')
raiz=doc.getroot()

#buscamos las regiones y las batallas, las añadimos a una lista con la que trabajaremos

lista=[]
for elem in raiz:
    listatemporal=[]
    listatemporal.append(elem.find("region").text)
    listatemporal.append(elem.find("nombre").text)
    lista.append(listatemporal)

print lista

#crear un diccionario desde una lista de listas