from lxml import etree
from funciones import *

monumentos = etree.parse('monumentos.xml')

menu="""
1.- Listar los monumentos
2.- Contar el numero de monumentos
3.- Dime una categoria y muestra todos los monumentos en esa categoria
4.- Buscar un monumento y mostrar toda su informacion
5.- Buscar todos los monumentos que empiezan por una cadena
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
        busqueda=input("Dime el nombre del monumento para buscar informacion: ")
        informacion=MostrarInformacion(monumentos,busqueda)
        print("---------------------------------------------")
        lista=[]
        for a in informacion:
            for b in a:
                lista.append(b)
        for c in lista:
            print(c)
            
        opcion=int(input("Elige una opción: "))
    
    if opcion==5:
        busqueda=input("Escribe una cadena para filtrar: ")
        municipios=BuscarCadena(monumentos,busqueda)
        for a in municipios:
            print(a)
        opcion=int(input("Elige una opción: "))
    
    if opcion== 6:
        break