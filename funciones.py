from lxml import etree

def Listarnombremonumentos(monumentos):
    lista=[]
    for monumentos in monumentos.xpath("//nombre/text()"):
        lista.append(monumentos)
    return lista

def ContarMonumentos(monumentos):
    lista=[]
    for monumentos in monumentos.xpath("//nombre/text()"):
        lista.append(monumentos)
    return len(lista)