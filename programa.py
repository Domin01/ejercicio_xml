from lxml import etree
from funciones import *

monumentos = etree.parse('monumentos.xml')

menu="""
1.- Listar los monumentos
2.- Contar el numero de monumentos
Opcion 3
Opcion 4
Opcion 5
"""
print(menu)
opcion=int(input("Elige una opción: "))

while opcion!=6:
    if opcion==1:
        municipios=Listarnombremonumentos(monumentos)
        for a in municipios:
            print(a)
        opcion=int(input("Elige una opción: "))
    
    if opcion==2:
        print(f"Hay un numero total de {ContarMonumentos(monumentos)}")
        opcion=int(input("Elige una opción: "))
    
    if opcion==3:

        municipios=Listarnombremonumentos(proyecto)
        for a in municipios:
            print(a)
        opcion=int(input("Elige una opción: "))
    
    if opcion==4:

        municipios=Listarnombremonumentos(proyecto)
        for a in municipios:
            print(a)
        opcion=int(input("Elige una opción: "))
    
    if opcion==5:

        municipios=Listarnombremonumentos(proyecto)
        for a in municipios:
            print(a)
        opcion=int(input("Elige una opción: "))
    
    if opcion== 6:
        break