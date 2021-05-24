from lxml import etree

def Listarnombremonumentos(monumentos):
    monumentos=monumentos.xpath("//nombre/text()")
    return monumentos

def ListarMonumentos(monumentos):
    monumentos=monumentos.xpath("//nombre/text()")
    return len(monumentos)

def ListarCategorias(monumentos):
    lista=[]
    for monumento in monumentos.xpath("//categorias/categoria/text()"):
        lista.append(monumento)
    lista = list(set(lista)) 
    return lista

def BuscarMonumentosCat(monumentos,busqueda):
    categorias=monumentos.xpath(f'//categorias[categoria="{busqueda}"]/../nombre/text()')
    return categorias

def MostrarInformacion(monumentos,busqueda):
    lista=[]
    informacion=monumentos.xpath(f'//directorio[nombre="{busqueda}"]')
    for a in informacion:
        lista.append(a.xpath("./nombre/text()"))
        lista.append(a.xpath("./web/text()"))
        lista.append(a.xpath("./telefono/text()"))
        lista.append(a.xpath("./fax/text()"))
        lista.append(a.xpath("./correo-electronico/text()"))
        lista.append(a.xpath("./direccion/text()"))
        lista.append(a.xpath("./locale/text()"))
    return lista

def BuscarCadena(monumentos,busqueda):
    informacion=monumentos.xpath(f'//directorio/nombre[contains(text(),"{busqueda}")]/text()')
    return informacion


#//book/author[contains(text(),'De')]: Devuelve los autores cuya información contine la subcadena “De”.
#/bookstore/book[title="Everyday Italian"]: Predicado que filtra de todos los nodos seleccionados con la ruta, aquellos que tienen un nodo hijo cuya información coincide con la indicada.
#/bookstore/book[year>2005]: En este caso se hace una comparación numérica.
#/bookstore/book/title[@lang="en"]: Ahora la selección se hace con un atributo.
#/bookstore/book/title[@lang="en"]/text(): Ejemplo igual que el anterior, pero en este caso se selecciona el nodo texto (información).
#//book[@category="CHILDREN" and price="29.99"]: Se pueden utilizar expresiones lógicas: and y or.