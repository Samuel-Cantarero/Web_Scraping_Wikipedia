# Importar bibliotecas
import requests
import re
import os
from pypdf import PdfReader

# Declarar y asignar una variable para las URLs y hacer la petición
urls = [
    'https://www.xunta.gal/dog/Publicados/2025/20250331/AnuncioG0767-250325-0006_gl.pdf',
    'https://www.juntadeandalucia.es/eboja/2025/47/BOJA25-047-00213-3298-01_00316903.pdf',
    'https://www.borm.es/services/boletin/ano/2025/numero/74/pdf',
    'https://doe.juntaex.es/pdfs/doe/2025/620o/620o.pdf',
    'https://dogv.gva.es/datos/2025/03/31/pdf/sumario_2025_10077_es.pdf',
    'https://www.bocm.es/boletin/CM_Boletin_BOCM/2025/03/31/BOCM-20250331076.PDF',
    'https://bocyl.jcyl.es/boletines/2025/03/31/pdf/BOCYL-S-31032025.pdf',
    'https://www.boa.aragon.es/cgi-bin/EBOA/BRSCGI?CMD=VEROBJ&MLKOB=1386037320303',
    'https://boc.cantabria.es/boces/verPdfAction.do?idBlob=39803&tipoPdf=0'
]

for url in urls:
    respuesta = requests.get(url)
    
# Descargar y crear archivo pdf
    with open('Comunidades-Prueba.pdf', 'wb') as f:
        f.write(respuesta.content)
    
# Abrir y leer el texto
    with open('Comunidades-Prueba.pdf', 'rb') as texto_BOE:
        leer_pdf = PdfReader(texto_BOE)
        
# Iterar cada página y extraer la información en formato texto
        contenido = ""
        for pagina in leer_pdf.pages:
            contenido += pagina.extract_text() 
    
# Utilizar expresiones regulares para buscar una palabra en el texto
    oposiciones = re.findall(r'Oposiciones+', contenido, re.IGNORECASE)
    
# Imprimir resultados encontrados
    print(oposiciones)

# Borrar pdf
os.remove('Comunidades-Prueba.pdf')