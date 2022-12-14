<h1>FPF3</h1>

Proyecto Integrador 2022 - Proyecto Alfa

<h2>Integrantes</h2>

<p>- Ferreyra Silvia</p>
<p>- Figueroa Gisela</p>
<p>- Parada Gonzalo</p>



<h2>Tema: Felicidad en el Mundo</h2>

<h3>Descripción del proyecto</h2>

El proyecto llevado a cabo se basa en la extracción de datos correspondientes a los índices de felicidad en los diferentes países del mundo.

Para llevar a cabo esta extracción, se trabaja sobre la página "principal", en la que se muestra una tabla general con nombres de paises, su posición actual en el ranking, un índice de felicidad, y su variación respecto al año anterior.

![image](https://user-images.githubusercontent.com/100076710/200549433-77f45b5b-e338-4baa-a19a-5f3dcaa27b68.png)


<h4>Primera idea</h4>

Como idea principal surge segmentar los datos por continentes, sorteando el primer inconveniente que se presenta: los países no tienen asociado ningun continente. Es por esto que se importa un archivo .csv, mediante el cual se analiza automaticamente su estructura y se le añaden los datos correspondientes a nuestro dataframe o base de datos. Ya con todos estos datos, se elabora un gráfico en el que se observan los índices segmentados por continente.

![image](https://user-images.githubusercontent.com/100076710/202066211-5d17cd3c-6971-45b3-a697-0999156022c9.png)


<h4>Segunda idea</h4>

La segunda idea es realizar un gráfico que muestre la variación del índice de felicidad de cada país, de manera individual, en el período comprendido por los últimos diez años. Para esto, el usuario ingresará el nombre de un país, que será filtrado de la base de datos, y en ese mismo instante se direccionará a la página correspondiente para hacer el segundo WebScraping. En esta etapa se recolectan los datos necesarios para elaborar un gráfico lineal, ordenado de la fecha más antigua a la fecha actual.

![image](https://user-images.githubusercontent.com/100076710/202066259-0019ba47-0ae0-420b-ab69-76a768d9e710.png)

Pagina utilizada para el web scraping: https://datosmacro.expansion.com/demografia/indice-felicidad

<h3>Librerías utilizadas</h2>

<p>- BeautifulSoup</p>
<p>- Pandas</p>
<p>- MatplotLib</p>
<p>- Requests</p>
<p>- csv</p>


<h2>Tablero de trabajo en Trello</h2>

<a href="https://trello.com/b/AIyzyE4v/proyecto-integrador">
Enlace al tablero
</a>

<h2>Aclaración para realizar ejecución!</h2>

Dejar en una misma carpeta estos tres archivos: 
<p>- PI_Modulo_Felicidad.py</p>
<p>- PI_Felicidad.py</p>
<p>- paises.csv</p>

<h2>Prueba 2, opcional!</h2>

Dejar en una misma carpeta estos tres archivos: 
<p>- PI_Felicidad_ConMySQL_PrimerScraping</p>
<p>- PI_Felicidad.py</p>
<p>- PI_Felicidad_ConMySQL.py</p>
<p>- paises.csv</p>

En este segundo método, ejecutar primero "PI_Felicidad_ConMySQL_PrimerScraping".
Luego trabajar con "PI_Felicidad_ConMySQL.py" para el análisis.
Crear previamente la base de datos adjunta en el script.

* No se muestra la totalidad de países porque solo se analizaron 60 (fué para agilizar el análisis y no se modificó sobre la hora de entrega por temor a que no funcione el código)

<h4>Tercera idea</h4>

Realizar junto con un archivo .csv ya extraido de una pagina web, el analisis de datos desde Power Bi. Para una mejor observacion y puesta de los datos en comparacion.


