from lxml import etree
from funciones import *

monumentos = etree.parse('monumentos.xml')

menu="""
1.- Listar los monumentos
2.- Contar el numero de monumentos
3.- Dime una categoria y muestra todos los monumentos en esa categoria
4.- Buscar un monumento y mostrar toda su informacion
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
        print(f"Hay un numero total de {ListarMonumentos(monumentos)} monumentos.")

        opcion=int(input("Elige una opción: "))
    
    if opcion==3:
        categorias=ListarCategorias(monumentos)
        for a in categorias:
            print(a)
        busqueda=input("Dime la categoria por la que quieres filtrar: ")
        cat=BuscarMonumentosCat(monumentos,busqueda)
        print("---------------------------------------------")
        for b in cat:
            print(b)
        opcion=int(input("Elige una opción: "))
    
    if opcion==4:
        busqueda=input("Dime el nombre del monumento para buscar: ")
        informacion=MostrarInformacion(monumentos,busqueda)
        print("---------------------------------------------")
        print(informacion)
        opcion=int(input("Elige una opción: "))
    
    if opcion==5:

        municipios=Listarnombremonumentos(proyecto)
        for a in municipios:
            print(a)
        opcion=int(input("Elige una opción: "))
    
    if opcion== 6:
        break