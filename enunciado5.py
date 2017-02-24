# -*- coding: utf-8 -*-
from lxml import etree
#
#Introduce el nombre de una zona, muestra el nombre del rey que haya ganado mayor numero de batallas en esa zona
#y del que mas batallas ha perdido junto con la suma de sus ejercitos en todas estas batallas
#
doc = etree.parse('batallasjuegotronos.xml')
raiz=doc.getroot()
