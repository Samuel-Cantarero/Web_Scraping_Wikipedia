# Importar bibliotecas
import requests
import re
import os
from pypdf import PdfReader

# definir función
def extraer_oposiciones(url):
    # Hacer la petición a la URL
    boe = requests.get(url)

    # Descargar y crear archivo pdf
    with open('BOE-Prueba.pdf', 'wb') as f:
        f.write(boe.content)

    # Abrir y leer el texto del PDF
    with open('BOE-Prueba.pdf', 'rb') as archivo:
        leer_pdf = PdfReader(archivo)
        contenido = ""

        # Iterar cada página y extraer la información en formato texto
        for pagina in leer_pdf.pages:
            contenido += pagina.extract_text()

    # Utilizar expresiones regulares para buscar una palabra en el texto
    oposiciones = []
    oposiciones.extend(re.findall(r'Oposiciones+', contenido, re.IGNORECASE))

    # Imprimir resultados encontrados
    print(oposiciones)

    # Borrar pdf
    os.remove('BOE-Prueba.pdf')

# Ejemplo de uso de la función
url = 'https://www.boe.es/boe/dias/2025/03/28/pdfs/BOE-S-2025-75.pdf'
extraer_oposiciones(url)