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

#he eliminado el caracter 'ñ' del xml porque xpath no aceptaba ese caracter a pesar de que ambos ficheros estan codificados con utf-8

rutarey="//rey_atacante/text()|//rey_defensor/text()"
ejercito="//ejercito_atacante[rey_atacante/text()='"+rey+"']/@ejercito"

reyes=raiz.xpath(rutarey)
if rey in reyes:
    ejercitos=raiz.xpath(ejercito)

#print ejercitos

#pasamos la lista de strings a una lista de numeros pero al mapear la lista como integer da una excepcion ValueError debido que no puede
#pasar a numero un valor como ' ' asi que usamos lo siguiente, la lista sin repetir y una estructura con la misma funcion que map(int,list)

x = list(set(ejercitos))

mayorejercito=0

for elem in x:
   if elem.strip():
       n = int(elem)
       if n>mayorejercito:
           mayorejercito=n

print mayorejercito

# falta modificar la ruta xpath ejercito para que tome tambien al rey en el ejercito defensor