Doc
===

ESP
---

El script `Trailers.py`_ requiere estar ubicado en una carpeta que contenga
un archivo de texto llamado `hoy.txt`_ y una carpeta llamada `Trailers`_
la ejecución de este script generará archivos de texto dentro de la carpeta
Trailers nombrados con las fechas de los siguientes dias de estrenos en los
próximos meses, cada archivo contendrá el nombre y el link de todos los estrenos
de ese dia, solo funciona una vez al día, ya que está realizado para su ejecucióna
automática al inicio del sistema, es necesario modificar el script para que funcione
ajustando los siguientes parámetros:

dir: Este parámetro debe contener la ubicación completa donde se ubica el script

link_estrenos: Aquí debe ir el link de tu página favorita que contenga la lista de
los próximos estrenos (explicación mas abajo), ej: "http://ejemplo.com/estrenos"


link_root: Aquí debe ir el link raiz de tu página de estrenos favorita (explicación
mas abajo), ej: "http://ejemplo.com"

Los links de estas páginas no se incluyen en el script ya que se debe elegir
la web de peliculas a la cual se tenga mas afinidad y guste mas, y asegurarse que
dicha página permita el scraping de su web antes de usarla.

Este script está escrito para ser combinado con `WinInicioApp`_ y hacer que se ejecute
al inicio del sistema.

La aplicación `TrailersReader.py`_ proporciona una interfaz gráfica para gestionar
los archivos generados. Un doble click en la película abre el link asociado a ella,
también es posible marcar películas como pendientes en un archivo "000-00-0.txt",
además es posible asociar una fecha a la película seleccionándola y eligiendo una
fecha en el botón ">".

ENG
---

The script `Trailers.py`_ requires being located in a folder which contains
a text file named `hoy.txt`_ and a folder named `Trailers`_
the execution of this script will generates text files inside the folder
Trailers named with the dates of the next releases days of the next
months, each file will contain the names and the links of that day,
this script only works once a day, since it is done to the execution at the
start of the system, it is necesary modify the script to it works
adjusting this parameters:

dir: This parameter must contain the full location of the script

link_estrenos: Here goes the link to your favorite releases webpages
(explanation below), ex: "http://example.com/releases"


link_root: Here goes the root link to your favorite webpage (explanation
below), ex: "http://example.com"

The links to this webpages are not included in the script because you have to choose
the film web to which you have more affinity and you like more, and make sure that
webpage alow the web scraping in his web.

This script is written to be combined with `WinInicioApp`_ and make it executable
at the start of the system.

The application `TrailersReader.py`_ gives a graphical interface to manage the files
generated. A double click on the film will open the link asociated to it,
it is posible to set pending film in a file named "000-00-0.txt",
you can asociate a date to a film selecting the film and chosing a date in the
button ">".

.. _`Trailers.py`: https://github.com/aglpy/Estrenos/tree/master/Trailers.py
.. _`hoy.txt`: https://github.com/aglpy/Estrenos/tree/master/hoy.txt
.. _`Trailers`: https://github.com/aglpy/Estrenos/tree/master/Trailers
.. _`WinInicioApp`: https://github.com/aglpy/utilities/tree/master/WinInicioApp
.. _`TrailersReader.py`: https://github.com/aglpy/Estrenos/tree/master/TrailersReader.py