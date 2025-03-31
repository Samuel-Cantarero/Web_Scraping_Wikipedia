# Importar bibliotecas
import requests
import re
import os
from pypdf import PdfReader

# Declarar y asignar una variable para la URL y hacer la petición
urls = [
    'https://www.boe.es/boe/dias/2025/03/28/pdfs/BOE-S-2025-75.pdf'
    'https://www.juntadeandalucia.es/eboja/2025/47/BOJA25-047-00213-3298-01_00316903.pdf'
]


for url in urls:
    response = requests.get(url)

# Descargar y crear archivo pdf
with open('BOE-Prueba.pdf', 'wb') as f:
    f.write(urls.content)

# Abrir y leer el texto
with open('BOE-Prueba.pdf', 'rb') as texto_BOE:
    leer_pdf = PdfReader(texto_BOE)

# Iterar cada página y extraer la información en formato texto
    contenido = ""
    for pagina in leer_pdf.pages:
        contenido += pagina.extract_text() if pagina.extract_text() else ""

# Utilizar expresiones regulares para buscar una palabra en el texto
oposiciones = re.findall(r'Oposiciones+', contenido, re.IGNORECASE)

# Imprimir resultados encontrados
print(oposiciones)

# Borrar pdf
os.remove('BOE-Prueba.pdf')