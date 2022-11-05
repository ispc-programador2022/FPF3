from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
import matplotlib.pyplot as plt

web= 'https://datosmacro.expansion.com/demografia/indice-felicidad'

result= requests.get(web)
content= result.text

soup= BeautifulSoup(result.content, 'html.parser')

#print(soup.prettify())

tabla= soup.find('div', class_='table-responsive').find('tbody').find_all('tr')

#Abro archivo csv que contiene contintentes con paises
dfContinentes = pd.read_csv(r'paises.csv')

#Creo un Dataframe vacío, que solo contiene las columnas, y un rango de valores determinado por el largo de la tabla extraida
df = pd.DataFrame(columns=['paises', 'ranking', 'indice', 'var', 'conti', 'enlace'],
                  index=range(len(tabla)))

posicionLlenado = 0        #Se usa para ir llenando fila por fila el dataframe, incrementandose en 1 cada vez que se llena.

listadoAnios = []
listadoIndices = []

for tabla in tabla:
  #Cambia la forma de llenado, se eliminan todas las LISTAS.
  #En cada variable se coloca el dato extraido, y se usan esas variables para llenar el DF al final de cada iteracion del FOR

  paisExtraido = tabla.find_all('td')[0].get_text()

  #Guardo acá la posición en la que se encuentra el primer corchete de apertura [+]
  #Ejemplo. En "ESPAÑA [+] el corchete esta en la posicion 7
  posicionCorte = paisExtraido.find('[')

  #Guardo acá el recorte, que va desde la posición CERO HASTA LA 7 donde está el corchete.
  #Se pondría paisExtraido[0:7]     [DESDE : HASTA]
  # El cero del inicio, por ser cero, se puede obviar...
  #La posicionCorte - 1 es para que elimine hasta el espacio en blanco que queda entre ESPAÑA y el corchete.
  paisFinal = (paisExtraido[: posicionCorte-1]).upper()


  nombreContinente = "SIN CONTINENTE"
  for x in range(len(dfContinentes)):
    #print(paisFinal, " -  - - ", dfContinentes.iloc[x, 0])
    if paisFinal == dfContinentes.iloc[x, 0]:
      nombreContinente = (dfContinentes.iloc[x, 5]).upper()

  ranking = (tabla.find_all('td')[1].get_text())
  #ACÁ, REPETIR LA LIMPIEZA PARA ELIMINAR EL "°". MISMOS PASOS A SEGUIR
  #ACÁ NO ES NECESARIO BUSCAR LA POSICION. SERIA [DESDE CERO : HASTA -1]   [:-1]
  #CON PONER -1 YA DETECTA QUE ES LA PRIMER POSICION CONTANDO DE DERECHA A IZQUIERDA

  indice = (tabla.find_all('td')[2].get_text())


  var = (tabla.find_all('td')[4].get_text())
  #REPETIR PARA ELIMINAR EL "%"
  #ACÁ NO ES NECESARIO BUSCAR LA POSICION. SERIA [DESDE CERO : HASTA -1]   [:-1]
  #CON PONER -1 YA DETECTA QUE ES LA PRIMER POSICION CONTANDO DE DERECHA A IZQUIERDA

  enlaces = (tabla.a.get('href'))

  df.iloc[posicionLlenado] = (paisFinal, ranking, indice, var, nombreContinente, enlaces)

  #Se incrementa la posicion, para que en la proxima iteracion del FOR llene la siguiente fila.
  posicionLlenado += 1

df.to_csv('Tabla_indicefelicidad.csv', index =False, sep =';', encoding='latin1')



#for cadaPais in enlaces:
#  print('www.pagina.com/seccion' + cadaPais)

#  df[(df.paises .isin(["Argentina [+]" , "Uruguay [+]"]))]

paisABuscar = input("Ingrese un país para obtener el promedio del indice de felicidad en los ultimos diez años: ")
encontrado = False
for x in range(len(df)):
  # print(paisFinal, " -  - - ", dfContinentes.iloc[x, 0])
  if paisABuscar.upper() == (df.iloc[x, 0]).upper():
    enlaceABuscar = "https://datosmacro.expansion.com" + (df.iloc[x, 5])
    encontrado = True
    print(enlaceABuscar)

if encontrado:
  # BUSCAR DATOS EN LA NUEVA PAGINA
  result2 = requests.get(enlaceABuscar)
  content2 = result2.text
  soup2 = BeautifulSoup(result2.content, 'html.parser')

  contenedorPais = soup2.select('tbody')
  listaDatosPorPais = []

  for fila in contenedorPais[0].find_all("tr"):
    for col in fila.find_all("td"):
      listaDatosPorPais.append(col.get_text().strip())

  contenedorPais = soup2.select('tbody')
  listaDos = []
  listaIndices = []

  for fila in contenedorPais:
    mifila = fila.find_all("tr")

    for colu in mifila:
      coluAnio = colu.find_all("td")[0]
      listaDos.append(coluAnio.get_text().strip())
      coluIndice = colu.find_all("td")[2]
      listaIndices.append(coluIndice.get_text().strip())

  #print(listaDos)
  #print(listaIndices)

  fig, ax = plt.subplots()


  ax.bar(listaDos, listaIndices)
  plt.suptitle(paisABuscar.upper())
  plt.title("Felicidad en los últimos diez años")
  plt.show()


else:
  print("El pais ingresado no ha sido encontrado en nuestra base de datos.")

