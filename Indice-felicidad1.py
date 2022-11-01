from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd

web= 'https://datosmacro.expansion.com/demografia/indice-felicidad'

result= requests.get(web)
content= result.text

soup= BeautifulSoup(result.content, 'html.parser')

#print(soup.prettify())

tabla= soup.find('div', class_='table-responsive').find('tbody').find_all('tr')

paises=[]

ranking= []

indice =[]

var = []
for tabla in tabla:
  paises.append(tabla.find_all('td')[0].get_text())
  ranking.append(tabla.find_all('td')[1].get_text())
  indice.append(tabla.find_all('td')[2].get_text())
  var.append(tabla.find_all('td')[4].get_text())

df = pd.DataFrame({'paises': paises, 'ranking': ranking, 'indice': indice, 'var': var})

df.to_csv('Tabla_indicefelicidad.csv', index =False, sep =';')
df