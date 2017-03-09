# -*- coding: utf-8 -*-
from lxml import etree
#
#Introduce el nombre de un rey y muestra el tamaño de su ejercito en la mayor batalla en la que haya participado
#
doc = etree.parse('batallasjuegotronos.xml')
raiz=doc.getroot()

#rey=raw_input("introduce el nombre de un rey")
#ej. Robb Stark,Stannis Baratheon
rey="Robb Stark"


#ejercitos=raiz.xpath("//batalla/contendientes")
#for i in ejercitos:
    #print i[0].attrib
    #print i.attrib[]


#for attr,value in ejercitos.items():
      #print attr,value

#raiz.findall("/batalla/contendientes/ejercito_atacante/rey_atacante")

rutarey="//rey_atacante/text()|//rey_defensor/text()"
reyes=raiz.xpath(rutarey)
if rey in reyes:
    ejercitos=("//ejercito_atacante[rey_atacante/text()="+rey+"]/@tamaño_ejercito")




