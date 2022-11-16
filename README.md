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

<h4>Segunda idea</h4>

La segunda idea es realizar un gráfico que muestre la variación del índice de felicidad de cada país, de manera individual, en el período comprendido por los últimos diez años. Para esto, el usuario ingresará el nombre de un país, que será filtrado de la base de datos, y en ese mismo instante se direccionará a la página correspondiente para hacer el segundo WebScraping. En esta etapa se recolectan los datos necesarios para elaborar un gráfico lineal, ordenado de la fecha más antigua a la fecha actual.


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
