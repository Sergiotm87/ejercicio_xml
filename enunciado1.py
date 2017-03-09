# -*- coding: utf-8 -*-
from lxml import etree
from collections import defaultdict
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

#uso un contenedor de tipo defaultdict, creamos un diccionario con las regiones como keys y las batallas como una lista de valores

#https://docs.python.org/2/library/collections.html#collections.defaultdict
#'Using list as the default_factory, it is easy to group a sequence of key-value pairs into a dictionary of lists'

dicregiones = defaultdict(list)
for k, v in lista:
        dicregiones[k].append(v)

#listar las batallas de cada region:

for key in dicregiones:
  print key, ":", dicregiones[key]