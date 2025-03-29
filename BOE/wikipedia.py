#Importar bibliotecas requests, BeautifulSoup y base de datos SQLITE
import requests
from bs4 import BeautifulSoup
import sqlite3

#Crear conexión a la base de datos y crear cursor
conexion = sqlite3.connect('base1')
cursor01 = conexion.cursor()

#Declaración y asignación de las variables para las dos urls
url_spain= "https://es.wikipedia.org/wiki/Espa%C3%B1a"
url_venezuela= "https://es.wikipedia.org/wiki/Venezuela"

#Crear objeto con la información de la web para España y crear el objeto donde se almacena la información en formato texto
respuesta_spain= requests.get(url_spain)
soup_spain = BeautifulSoup(respuesta_spain.text, "html.parser")

#Crear un objeto con la información del elemento sup con identificador concreto
sup_spain = soup_spain.find('sup', {'id': 'cite_ref-45'})

#Crear un objeto con el primer elemento span posterior al objeto sup creado y que contiene la información de la población 
span_spain = sup_spain.find_next('span',{'style': 'white-space:nowrap'})

#Imprimir población de España.
poblacion_spain = span_spain.text
print(poblacion_spain)

#Crear un objeto con la información del elemento a con identificador concreto
a_spain= soup_spain.find('a', {'title': 'Cuatro Torres Business Area'})

#Crear un objeto con el primer elemento p posterior al objeto a creado y que contiene la información del PIB
p_spain= a_spain.find_next('p')

#Imprimir el PIB de España. 
PIB_spain = p_spain.text
print(PIB_spain) 

#Subir los datos a la base de datos.
dato_spain = ('Spain', poblacion_spain, PIB_spain)
consulta = "INSERT INTO Spain ('Pais', 'Poblacion', 'PIB') values (?,?,?)"
cursor01.execute (consulta, dato_spain)
conexion.commit()

#Crear objeto con la información de la web para Venezuela y crear el objeto donde se almacena la información en formato texto
respuesta_venezuela= requests.get(url_venezuela)
soup_venezuela = BeautifulSoup(respuesta_venezuela.text, "html.parser")

#Crear un objeto con la información del elemento sup con identificador concreto
sup_venezuela = soup_venezuela.find('sup', {'id': 'cite_ref-289'})

#Crear un objeto con el primer elemento p anterior al objeto sup creado y que contiene la información de la población
parrafo_venezuela = sup_venezuela.find_previous('p')

#Imprimir población de Venezuela. He tenido que poner encode utf-8 porque me da problemas con algunas letras
poblacion_venezuela = parrafo_venezuela.text
print(poblacion_venezuela)

#Crear un objeto con la información del elemento a
a_venezuela = soup_venezuela.find('a', {'title': 'Economía de Venezuela'})

#Crear un objeto con el primer elemento p posterior al objeto a creado y que contiene la información del PIB
p_venezuela = a_venezuela.find_next('p')

#Imprimir el PIB de Venezuela. He tenido que poner encode utf-8 porque me da problemas con algunas letras
PIB_venezuela = p_venezuela.text
print(PIB_venezuela)

#Subir los datos a la base de datos.
dato_venezuela = ('Venezuela', poblacion_venezuela, PIB_venezuela)
consulta2 = "INSERT INTO Venezuela ('Pais', 'Poblacion', 'PIB') values (?,?,?)"
cursor01.execute (consulta2, dato_venezuela)
conexion.commit()

#Desconectar base de datos.
conexion.close()