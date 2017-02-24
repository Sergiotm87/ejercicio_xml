# -*- coding: utf-8 -*-
from lxml import etree
#
#    Muestra todas las batallas ordenadas por la region en la que se produjeron
#
doc = etree.parse('batallasjuegotronos.xml')
raiz=doc.getroot()
