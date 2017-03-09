# -*- coding: utf-8 -*-
from lxml import etree
#
#Cuenta cuantas batallas se han producido de cada tipo
#
doc = etree.parse('batallasjuegotronos.xml')
raiz=doc.getroot()

#tomamos los tipos de batallas que hay en una lista

tiposlist=[]

for elem in raiz:
    tiposlist.append(elem.get("tipo_batalla"))


#eliminamos duplicados

x = list(set(tiposlist))


#contamos apariciones de cada elemento de la lista sin repetir en la lista completa y lo mostramos

for elem in x:
    print "Battallas tipo",elem,":",tiposlist.count(elem)
