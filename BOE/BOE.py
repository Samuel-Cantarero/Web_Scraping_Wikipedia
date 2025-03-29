#Importar bibliotecas
import requests
import re
from pypdf import PdfReader

#Declarar y asignar una variable para la URL y hacer la petición
URL = 'https://www.boe.es/boe/dias/2025/03/28/pdfs/BOE-S-2025-75.pdf'
BOE = requests.get(URL)  

#Descargar y crear archivo pdf
with open('BOE-Prueba.pdf', 'wb') as f:
    f.write(BOE.content)

# Abir y leer el texto
texto_BOE = open('BOE-Prueba.pdf', 'rb')
leer_pdf = PdfReader(texto_BOE)

# Iterar cada página y extraer la información en formato texto
contenido =""
for pagina in leer_pdf.pages:
    contenido += pagina.extract_text()

#Utilizar expresiones regulares para buscar una palabra en el texto
oposiciones = []
oposiciones.extend (re.findall('Oposiciones+', contenido, re.IGNORECASE))

#Imprimir resultados encontrados
print (oposiciones)