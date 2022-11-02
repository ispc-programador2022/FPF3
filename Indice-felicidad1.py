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
enlaces = []
var = []

for tabla in tabla:
  paisExtraido = tabla.find_all('td')[0].get_text()

  #Guardo acá la posición en la que se encuentra el primer corchete de apertura [+]
  #Ejemplo. En "ESPAÑA [+] el corchete esta en la posicion 7
  posicionCorte = paisExtraido.find('[')

  #Guardo acá el recorte, que va desde la posición CERO HASTA LA 7 donde está el corchete.
  #Se pondría paisExtraido[0:7]     [DESDE : HASTA]
  # El cero del inicio, por ser cero, se puede obviar...
  #La posicionCorte - 1 es para que elimine hasta el espacio en blanco que queda entre ESPAÑA y el corchete.
  paisFinal = paisExtraido[: posicionCorte-1]

  #UNA VEZ QUE ESTÁ LIMPIO EL NOMBRE DEL PAIS, LO AGREGO A LA LISTA DE PAISES
  paises.append(paisFinal)

  ranking.append(tabla.find_all('td')[1].get_text())
  #ACÁ, REPETIR LA LIMPIEZA PARA ELIMINAR EL "°". MISMOS PASOS A SEGUIR
  #ACÁ NO ES NECESARIO BUSCAR LA POSICION. SERIA [DESDE CERO : HASTA -1]   [:-1]
  #CON PONER -1 YA DETECTA QUE ES LA PRIMER POSICION CONTANDO DE DERECHA A IZQUIERDA

  indice.append(tabla.find_all('td')[2].get_text())


  var.append(tabla.find_all('td')[4].get_text())
  #REPETIR PARA ELIMINAR EL "%"
  #ACÁ NO ES NECESARIO BUSCAR LA POSICION. SERIA [DESDE CERO : HASTA -1]   [:-1]
  #CON PONER -1 YA DETECTA QUE ES LA PRIMER POSICION CONTANDO DE DERECHA A IZQUIERDA

  enlaces.append(tabla.a.get('href'))

df = pd.DataFrame({'paises': paises, 'ranking': ranking, 'indice': indice, 'var': var, 'enlace': enlaces})
df.to_csv('Tabla_indicefelicidad.csv', index =False, sep =';')
print(df)


#for cadaPais in enlaces:
#  print('www.pagina.com/seccion' + cadaPais)

#  df[(df.paises .isin(["Argentina [+]" , "Uruguay [+]"]))]
