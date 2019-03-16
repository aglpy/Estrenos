#******************************************************************************
#Se ejecuta solo una vez al dia, requiere la existencia de un archivo ./hoy.txt
#y la existencia de una carpeta ./Trailers/, tras ejecutarse guarda en la carpeta
#Trailer archivos de texto con las fechas y contiene los estrenos próximos y los
#links de "tu página favorita" a estas peliculas
#@angalaagl
#https://github.com/aglpy
#https://anaconda.org/angala
#******************************************************************************
import datetime
import os.path
import time
import urllib.request

from bs4 import BeautifulSoup

dir = "D:\DATA\PS\Trailers" #Directorio actual

hoy_arch = dir + "/hoy.txt" #Archivo para controlar una única ejecución diaria
directorio = dir + "./Trailers/" #Carpeta donde se guardarán los links
link_estrenos = "Look at docs" #Pagina donde están los estrenos de España
link_root = "Look at docs" #Usado para obtener el link completo de cada peli
parser = "lxml" #Parser que usa BeautifulSoup

def dias(body): #Devuelve un array con los dias disponibles en body
	return body.find_all("div", attrs={"id":"main-wrapper-rdcat"})

def fecha(dia): #Devuelve la fecha del dia
	return dia.find("div", attrs={"class":"rdate-cat"})["id"]

def pelis(dia): #Devuelve un array con todas las pelis en el dia dado
	return dia.find_all("div", attrs={"class":"top-movie"})

def titulo(peli): #Devuelve el titulo de la peli
	return peli.find("div", attrs={"class":"mc-right"}).find("h3").find("a")["title"]
	
def link(peli): #Devuelve el link completo de la peli
	return link_root +\
	peli.find("div", attrs={"class":"mc-right"}).find("h3").find("a")["href"]

with open(hoy_arch, "r") as arch: #Lee el ultimo dia ejecutado
	ulti_dia = arch.read()
if ulti_dia != str(datetime.date.today()): #Solo se ejecuta si nos e ha ejecutado hoy
	with open(hoy_arch, "w") as arch: #Se guarda hoy como ultimo dia ejecutado
		arch.write(str(datetime.date.today()))
	
	pag = urllib.request.urlopen(link_estrenos) #Obtenemos el html
	body = BeautifulSoup(pag, parser) #Creamos el parseable

	for dia in dias(body): #Para cada dia que aparezca en la pagina
		print("\n" + fecha(dia) + "\n")
		with open(directorio + fecha(dia) + ".txt", "w") as arch: #Creamos un archivo con la fecha
			for peli in pelis(dia): #Para cada peli en ese dia
				print(titulo(peli))
				arch.write(titulo(peli) + "\n") #Escribimos el nombre de la peli en el archivo
				arch.write("	" + link(peli) + "\n") #Escribimos el link tabulado en el archivo
				arch.write("\n") #Dejamos un espacio tras cada peli
	print("\nFIN")
	time.sleep(5)