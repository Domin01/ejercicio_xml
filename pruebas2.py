from lxml import etree

doc = etree.parse("proyecto.xml")

for a in doc.xpath("//nombre/text()"):
	print (a)