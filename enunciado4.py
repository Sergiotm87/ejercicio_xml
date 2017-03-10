# -*- coding: utf-8 -*-
from lxml import etree
#
#Introduce el nombre de un rey y muestra el tamaño de su ejercito en la mayor batalla en la que haya participado
#
doc = etree.parse('batallasjuegotronos.xml')
raiz=doc.getroot()

rey=raw_input("introduce el nombre de un rey: ")
#ej. Robb Stark,Stannis Baratheon
#rey="Robb Stark"

#he eliminado el caracter 'ñ' del xml porque xpath no aceptaba ese caracter a pesar de que ambos ficheros estan codificados con utf-8

rutarey="//rey_atacante/text()|//rey_defensor/text()"
ejercito="//ejercito_atacante[rey_atacante/text()='"+rey+"']/@ejercito| //ejercito_defensor[rey_defensor/text()='"+rey+"']/@ejercito"

#obtenemos la lista de reyes y si el nombre introducido se encuetra en él obtiene el tamaño de sus ejercitos en las diferentes batallas
reyes=raiz.xpath(rutarey)
if rey in reyes:
    ejercitos=raiz.xpath(ejercito)
    #pasamos la lista de strings a una lista de numeros pero al mapear la lista como integer da una excepcion ValueError debido que no puede
    #pasar a numero un valor como ' ' asi que usamos lo siguiente, la lista sin repetir y una estructura con la misma funcion que map(int,list)
    #y obtenemos el mayor ejercito con el que ha participado en una batalla
    x = list(set(ejercitos))
    mayorejercito=0
    for elem in x:
       if elem.strip():
           n = int(elem)
           if n>mayorejercito:
               mayorejercito=n
    #ruta con el mismo nodo padre, obtenemos el tamaño del ejercito contrincante del mayor ejercito del rey introducido:
    ejenemigo="//contendientes/ejercito_atacante[@ejercito="+str(mayorejercito)+"][//rey_atacante/text()='"+rey+"']/following-sibling::ejercito_defensor"
    enemigo=raiz.xpath(ejenemigo)
    ejercitoenemigo= int(enemigo[0].get('ejercito'))
    rutanombre="//batalla/contendientes[((ejercito_atacante/@ejercito='15000' or ejercito_defensor/@ejercito='15000') and (ejercito_atacante/@ejercito='4000' or ejercito_defensor/@ejercito='4000')) and //rey_atacante/text()='Joffrey/Tommen Baratheon']/../nombre/text()"
    nombrebatalla=raiz.xpath(rutanombre)
    print "\nla mayor batalla de "+rey+" es "+nombrebatalla[0]+" en la que participaron "+str(mayorejercito+ejercitoenemigo)+" hombres"
else:
    print "nombre introducido no válido"