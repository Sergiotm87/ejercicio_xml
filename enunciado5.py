# -*- coding: utf-8 -*-
from lxml import etree
#
#Introduce el nombre de una zona, muestra el nombre del rey que haya ganado mayor numero de batallas en esa zona
#y del que mas batallas ha perdido junto con la suma de sus ejercitos en todas estas batallas
#
doc = etree.parse('batallasjuegotronos.xml')
raiz=doc.getroot()

#zona=raw_input("introduce el nombre de una zona")
#ej. Deepwood Motte,Winterfell
zona="Deepwood Motte"

#localizamos el nombre de las zonas, despues tomamos los reyes que hayan participado en esas zonas y tomamos el valor con mayor numero de
#coincidencias cuyo resultado sea victoria
rutazona="//localizacion/text()"
zonas=raiz.xpath(rutazona)


#rutareyes="//rey_atacante/text()[//localizacion/text()='"+zona+"']"
#reyes=raiz.xpath(rutareyes)
#print len(reyes)
##tomar el valor con mayor numero de ocurrencias de una lista:
#a=max(set(reyes), key=reyes.count)
#falta comprobar resultado = victoria
#//batalla[//rey_atacante/text()|localizacion/text()='Winterfell']
#//batalla[localizacion/text()='Winterfell'][rey_atacante/text()]
#(//rey_atacante/text()|//rey_defensor/text())/../..

l=[]

if zona in zonas:
    for elem in raiz:
        if elem.find("localizacion").text ==zona and elem.find("resultado_atacante").text=="win":
            #dic={}
            #dic[elem.find("contendientes/ejercito_atacante/rey_atacante").text]=1
            #l.append(dic)
            l.append(elem.find("contendientes/ejercito_atacante/rey_atacante").text)

print l

#print dic

#falta comprobar si es mas intuitivo usar lista o diccionario y contar ocurrencias de cada elemento