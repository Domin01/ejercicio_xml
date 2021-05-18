from lxml import etree

### Ejercicio 1
def Listarnombremonumentos(proyecto):
    lista=[]
    for monumentos in proyecto.xpath("//nombre/text()"):
        lista.append(monumentos)
    return lista