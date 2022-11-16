import numpy as np
from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
from PI_Modulo_Felicidad import *


web= 'https://datosmacro.expansion.com/demografia/indice-felicidad'
result= requests.get(web)
content= result.text
soup= BeautifulSoup(result.content, 'html.parser')

tabla= soup.find('div', class_='table-responsive').find('tbody').find_all('tr')

#Abro y Leo archivo csv que contiene contintentes con paises
dfContinentes = pd.read_csv(r'paises.csv')

posicionLlenado = 0        #Se usa para ir llenando fila por fila la BDD, incrementandose en 1 cada vez que se llena.

listadoAnios = []
listadoIndices = []

for tabla in tabla:
  paisExtraido = tabla.find_all('td')[0].get_text()
  posicionCorte = paisExtraido.find('[')
  paisFinal = (paisExtraido[: posicionCorte-1]).upper()

  nombreContinente = "SIN CONTINENTE"
  for x in range(len(dfContinentes)):
    if paisFinal == dfContinentes.iloc[x, 0].upper():
      nombreContinente = (dfContinentes.iloc[x, 6]).upper()

  ranking = (tabla.find_all('td')[1].get_text())
  ranking = ranking[:-1]

  indice = (tabla.find_all('td')[2].get_text())
  indice = indice.replace(",", ".")

  var = (tabla.find_all('td')[4].get_text())
  var = var[:-1] #Elimino %

  enlaces = (tabla.a.get('href'))

  guardarEnMySql(paisFinal, ranking, indice, var, nombreContinente, enlaces)

  #Se incrementa la posicion, para que en la proxima iteracion del FOR llene la siguiente fila.
  posicionLlenado += 1

print("Información almacenada en la base de datos.")