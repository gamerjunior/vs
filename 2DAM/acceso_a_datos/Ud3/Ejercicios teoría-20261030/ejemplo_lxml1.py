
from lxml import etree

with open('planetas.html') as fs:
    cadena_html = fs.read()

html = etree.HTML(cadena_html)
result = etree.tostring(html, pretty_print=False, method="html")
print(result.decode())
