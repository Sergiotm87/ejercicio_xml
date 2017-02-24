# -*- coding: utf-8 -*-
from lxml import etree
#
#Cuenta cuantas batallas se han producido de cada tipo
#
doc = etree.parse('batallasjuegotronos.xml')
raiz=doc.getroot()
