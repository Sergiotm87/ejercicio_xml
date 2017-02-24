# -*- coding: utf-8 -*-
from lxml import etree
#
#Introduce el apellido de una casa y muestra todos los miembros de esa familia que hayan participado en alguna batalla
#
doc = etree.parse('batallasjuegotronos.xml')
raiz=doc.getroot()
