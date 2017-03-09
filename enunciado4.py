# -*- coding: utf-8 -*-
from lxml import etree
#
#Introduce el nombre de un rey y muestra el tamaño de su ejercito en la mayor batalla en la que haya participado
#
doc = etree.parse('batallasjuegotronos.xml')
raiz=doc.getroot()

#for e in raiz.findall('//attribute::tamaño_ejercito'):
    #print e
