import matplotlib.pyplot as plt
from datetime import datetime
import pymysql


def conectarse():
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        db="pruebapy"
    )
    return connection


def guardarEnMySql(nom, ran, ind, variacion, conti, enl):
    co = conectarse()

    cursor = co.cursor()
    sql = f"INSERT INTO paises(nombre, ranking, indice, variacion, continente, enlace) VALUES ('{nom}', '{ran}', '{ind}', '{variacion}', '{conti}', '{enl}')"
    cursor.execute(sql)
    co.commit()

def consultarEnlace(paisBuscado):
    co = conectarse()

    cursor = co.cursor()
    sql = f"SELECT enlace FROM paises where nombre = '{paisBuscado}'"
    cursor.execute(sql)
    tuplaObtenida = cursor.fetchall()
    return tuplaObtenida

def consultarPorContinente(continenteBuscado):
    co = conectarse()

    cursor = co.cursor()
    sql = f"SELECT nombre, indice FROM paises where continente = '{continenteBuscado}' order by indice DESC"
    cursor.execute(sql)
    tupla2Obtenida = cursor.fetchall()
    return tupla2Obtenida


def menuPrincipal():
  print("\n")
  print("*************************************")
  print("Menú Principal")
  print("*************************************")
  print("\n")
  print("1 - Consultar indice de felicidad de un país en los últimos 10 años.")
  print("2 - Consultar índices por continentes.")
  print("0 - Salir")
  print("\n")

  return (input("Ingrese el número correspondiente según la opción que desee: "))


def menuContinentes():
  print("\n \n")
  print("Continentes para analizar: ")
  print("")
  print("1 - África")
  print("2 - América")
  print("3 - Asia")
  print("4 - Europa")
  print("5 - Oceanía")
  print("0 - Cancelar")
  print("\n \n")
  return (input("Ingrese el continente elegido: "))

def crearGraficoContinentes(continenteElegido, paises, indices):
    figura1, ejes = plt.subplots()
    # Colocamos una etiqueta en el eje Y
    ejes.set_ylabel("Indices de felicidad", fontdict={'fontsize': 14, 'fontweight': 'bold'})
    ejes.set_xlabel("Paises", fontdict={'fontsize': 14, 'fontweight': 'bold'})

    # Creamos la grafica de barras utilizando 'paises' como eje X y 'ventas' como eje y.
    plt.bar(paises, indices, color="green", width=0.25)

    ejes.grid(axis='y', color='gray', linestyle='dashed')
    #Agrega color al fondo del grafico
    #ejes.set_facecolor('y')
    plt.title("Indice de felicidad en paises de " + continenteElegido, fontdict = {'fontsize':20, 'fontweight':'bold', 'color':'tab:blue'})
    plt.xticks(rotation=90)

    hora = str(datetime.now())
    hora = hora.replace('.', ' ')
    hora = hora.replace(':', ' ')
    guardarComo = f"Grafico {continenteElegido} {hora}.jpg"


    plt.savefig(guardarComo)

    # Finalmente mostramos la grafica con el metodo show()
    plt.show()

    # ejes.bar(listaNombrePais, listaIndicePais)

def crearGraficoPaises(pais, Anios, Indices):
  figura2, ejes2 = plt.subplots()

  ejes2.plot(Anios, Indices, color="red", marker = 'o')
  plt.title("Felicidad en los últimos diez años en " + pais.upper(), fontdict = {'fontsize':20, 'fontweight':'bold', 'color':'tab:blue'})
  plt.xticks(rotation=90)

  ejes2.set_ylabel("Índices de felicidad", fontdict = {'fontsize':14, 'fontweight':'bold'})
  ejes2.set_xlabel("Años", fontdict = {'fontsize':14, 'fontweight':'bold'})
  ejes2.set_xticks(Anios)
  ejes2.grid(axis='both', color='gray', linestyle='dashed')

  hora = str(datetime.now())
  hora = hora.replace('.', ' ')
  hora = hora.replace(':', ' ')
  guardarComo = f"Grafico {pais} {hora}.jpg"


  plt.savefig(guardarComo)

  plt.show()
