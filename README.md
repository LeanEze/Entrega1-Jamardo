# Entrega1-Jamardo

 Descripcion

Esta aplicacion permite ingresar a un sitio web donde se pueden realizar las siguientes funciones:

1. Ingresar formularios con datos de tres tipos de animales y guardarlos en una base de datos.

2. Consultar los datos ingresados en dicha base de datos.



Ejecucion del programa

- Instalación:
Para poder instalar el software se necesita:

1- Chequear la version de python instalada
Para poder ejecutar el programa sin problemas recomendamos versiones 3.8.0 o superiores.
    Como chequear tu version de python:
    Ingresar a la terminal
    
    Para ios o linux:

    python –version

    Python 3.8.0

    En windows:

    c:\> py –version

    c:\> Python 3.8.0


Instalar Dependencias:

Para esto es necesario que ejecutes pip install, asegurarte que estas en la carpeta correspondiente al proyecyo y que puedas ver la carpeta requiremets.txt.

> pip install -r requirements.txt

Esto te va a devolver mucho codigo dentro de la terminal

(Algunos sistemas operativos necesitan que uses pip3 en vez de pip)

Setear la Aplicacion Django:

Una vez que finalizaste la instalación de dependencias necesitas correr algunos comandos de django.

    -Migrations

Inicializar la base de datos (ios o linux):

> python mananage.py migrate

En windows:

c:\> py mananage.py migrate

    Ejecutar el servidor:

> python mananage.py runserver

windows:

c:\> py mananage.py runserver

De esta manera el servidor proporciona la ruta de la aplicacion en la terminal. Copiar la direccion y utilizarla en un navegador web y seleccionar la ruta "inicio/"


Utilizacion de finciones del programa

Desde el inicio puede ver la barra de opciones donded se pueden realizar las siguientes funciones.

1. Inicio: se describen las funciones y si se utilizaz dentro de la misma permite actualizar la pagina. si se utiliza fuera de la misma ingresara nuevamente.

2. Perros: dedntro se encuentra un formulario donde debe completarse con datos de perros y se guardaran en una base de datos.

3. Gatos: dedntro se encuentra un formulario donde debe completarse con datos de gatos y se guardaran en una base de datos.

4. Cerdos: dedntro se encuentra un formulario donde debe completarse con datos de cerdos y se guardaran en una base de datos.

5. Busqueda en formularios: te permit buscar con el nombre del animal dentro de la base de datos donde se guardaron los formularios ingresados. 





