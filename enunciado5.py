# -*- coding: utf-8 -*-
from lxml import etree
#
#Introduce el nombre de una zona, muestra el nombre del rey que haya ganado mayor numero de batallas en esa zona
#y del que mas batallas ha perdido junto con la suma de sus ejercitos en todas estas batallas
#
doc = etree.parse('batallasjuegotronos.xml')
raiz=doc.getroot()

zona=raw_input("introduce el nombre de una zona")
#ej. Deepwood Motte,Winterfell

#localizamos el nombre de las zonas, despues tomamos los reyes que hayan participado en esas zonas y tomamos el valor con mayor numero de
#coincidencias cuyo resultado sea victoria

rutazona="//localizacion/text()"

rutareyes="//rey_atacante/text()[//localizacion/text()='"+zona+"']"

#falta comprobar resultado = victoria