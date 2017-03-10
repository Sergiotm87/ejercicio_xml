# -*- coding: utf-8 -*-
from lxml import etree
#
#Introduce el nombre de una zona, muestra el nombre del rey que haya ganado mayor numero de batallas en esa zona
#y del que mas batallas ha perdido junto con la suma de sus ejercitos en todas estas batallas
#
doc = etree.parse('batallasjuegotronos.xml')
raiz=doc.getroot()

#zona=raw_input("introduce el nombre de una zona")
#ej. The Riverlands,The North,The Westerlands
zona="The Riverlands"

#localizamos el nombre de las zonas, despues tomamos los reyes que hayan participado en esas zonas y tomamos el valor con mayor numero de
#coincidencias cuyo resultado sea victoria
rutazona="//region/text()"
zonas=raiz.xpath(rutazona)


l=[]

lperdedor=[]

atacante="contendientes/ejercito_atacante/rey_atacante"
defensor="contendientes/ejercito_defensor/rey_defensor"

if zona in zonas:
    for elem in raiz:
        if elem.find("region").text ==zona:
            if elem.find("resultado_atacante").text=="win":
                l.append(elem.find(atacante).text)
            if elem.find("resultado_atacante").text!="win":
                l.append(elem.find(defensor).text)
            if elem.find("resultado_atacante").text=="win":
                lperdedor.append(elem.find(defensor).text)
            if elem.find("resultado_atacante").text!="win":
                lperdedor.append(elem.find(atacante).text)



#genero un diccionario que toma como clave cada elemento sin repetir de la lista y como valor el numero de ocurrencias
#de ese elemento del que tomamos la clave con el valor más alto

numvictorias=dict((x,l.count(x)) for x in set(l))
maxvencedor = max(numvictorias, key=numvictorias.get)

numderrotas=dict((x,lperdedor.count(x)) for x in set(lperdedor))
maxperdedor = max(numderrotas, key=numderrotas.get)


print "El rey con más batallas ganadas en",zona,"es",maxvencedor
print "El que ha perdido más batallas en",zona,"es",maxperdedor