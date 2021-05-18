from lxml import etree
from funciones import *

proyecto = etree.parse('proyecto.xml')

menu="""Opcion 1
Opcion 2
Opcion 3
Opcion 4
Opcion 5
"""
print(menu)
opcion=int(input("Elige una opción: "))

while opcion != 6:
    if opcion == 1:
        municipios=Listarnombremonumentos(proyecto)
        for a in municipios:
            print(a)
        opcion=int(input("Elige una opción: "))