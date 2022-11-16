import numpy as np
from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
import matplotlib.pyplot as plt
from PI_Modulo_Felicidad import *


web= 'https://datosmacro.expansion.com/demografia/indice-felicidad'
result= requests.get(web)
content= result.text
soup= BeautifulSoup(result.content, 'html.parser')

tabla= soup.find('div', class_='table-responsive').find('tbody').find_all('tr')

#Abro y Leo archivo csv que contiene contintentes con paises
dfContinentes = pd.read_csv(r'paises.csv')

#Creo un Dataframe vacío, que solo contiene las columnas, y un rango de valores determinado por el largo de la tabla extraida
df = pd.DataFrame(columns=['paises', 'ranking', 'indice', 'var', 'conti', 'enlace'],
                  index=range(len(tabla)))

posicionLlenado = 0        #Se usa para ir llenando fila por fila el dataframe, incrementandose en 1 cada vez que se llena.

listadoAnios = []
listadoIndices = []

for tabla in tabla:
  #En cada variable se coloca el dato extraido, y se usan esas variables para llenar el DF al final de cada iteracion del FOR

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

  #Lleno DF
  df.iloc[posicionLlenado] = (paisFinal, ranking, indice, var, nombreContinente, enlaces)
  lista_orden= df.sort_values(by=['indice'], ascending=False)
  #print(lista_orden)
  lista_orden.to_csv('Tabla_indicefelicidad.csv', index =False, sep =';')
  #print(lista_orden)
  #Se incrementa la posicion, para que en la proxima iteracion del FOR llene la siguiente fila.
  posicionLlenado += 1

  lista_orden.to_csv('Tabla_indicefelicidad.csv', index =False, sep =';', encoding='latin1')

opcion = menuPrincipal()

while opcion != "0":
  if opcion == "1":
    paisABuscar = input("\n \nIngrese un país para obtener el promedio del indice de felicidad en los ultimos diez años: ")
    encontrado = False

    for x in range(len(df)):
      if paisABuscar.upper() == (df.iloc[x, 0]).upper():
        enlaceABuscar = "https://datosmacro.expansion.com" + (df.iloc[x, 5])
        encontrado = True

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
      listaAnios = []
      listaIndices = []

      #RECORRO AL REVES EL FOR PARA OBTENER DE AÑO MAS VIEJO A MAS NUEVO
      for fila in contenedorPais[::-1]:
        mifila = fila.find_all("tr")

        for colu in mifila:
          coluAnio = colu.find_all("td")[0]
          listaAnios.append(int(coluAnio.get_text().strip()))
          coluIndice = colu.find_all("td")[2]
          coluIndice = coluIndice.get_text().strip()
          coluIndice = coluIndice.replace(",", ".")
          listaIndices.append(float(coluIndice))

      crearGraficoPaises(paisABuscar, listaAnios, listaIndices)

    else:
      print("\n \nEl pais ingresado no ha sido encontrado en nuestra base de datos.")

    opcion = menuPrincipal()

  elif opcion == "2":
    opcionContinente = menuContinentes()

    while opcionContinente != "0":
      if opcionContinente == "1":
        continenteElegido = 'ÁFRICA'
        break
      elif opcionContinente == "2":
        continenteElegido = 'AMÉRICA'
        break
      elif opcionContinente == "3":
        continenteElegido = 'ASIA'
        break
      elif opcionContinente == "4":
        continenteElegido = 'EUROPA'
        break
      elif opcionContinente == "5":
        continenteElegido = 'AUSTRALIA Y OCEANÍA'
        break
      else:
        print("\n \nOpción no disponible. Recuerde ingresar un numero entero que se encuentre en las opciones del menú")
        opcionContinente = menuContinentes()

    if opcionContinente == 0:
      print("Nos vemos pronto! Que seas Felíz!")
      exit()

    else:
      listaNombrePais = []
      listaIndicePais = []

      for x in range(len(df)):
      #for x in range(len(df)):
          if df.iloc[x, 4] == continenteElegido:
            listaNombrePais.append((df.iloc[x, 0]))
            listaIndicePais.append(float((df.iloc[x, 2])))

      crearGraficoContinentes(continenteElegido, listaNombrePais, listaIndicePais)

    opcion = menuPrincipal()

  else:
    print("\n \nOpción no disponible. Recuerde ingresar un numero entero que se encuentre en las opciones del menú")
    opcion = menuPrincipal()

print("\n \nPrograma finalizado!")
