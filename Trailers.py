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

dir = "D:\DATA\PS\Trailers"

hoy_arch = dir + "/hoy.txt"
directorio = dir + "./Trailers/"
link_estrenos = "Look at docs"
link_root = "Look at docs"
parser = "lxml"

def dias(body):
	return body.find_all("div", attrs={"id":"main-wrapper-rdcat"})

def fecha(dia):
	return dia.find("div", attrs={"class":"rdate-cat"})["id"]

def pelis(dia):
	return dia.find_all("div", attrs={"class":"top-movie"})

def titulo(peli):
	return peli.find("div", attrs={"class":"mc-right"}).find("h3").find("a")["title"]
	
def link(peli):
	return link_root +\
	peli.find("div", attrs={"class":"mc-right"}).find("h3").find("a")["href"]

with open(hoy_arch, "r") as arch:
	ulti_dia = arch.read()
if ulti_dia != str(datetime.date.today()):
	with open(hoy_arch, "w") as arch:
		arch.write(str(datetime.date.today()))
	
	pag = urllib.request.urlopen(link_estrenos)
	body = BeautifulSoup(pag, parser)

	for dia in dias(body):
		print("\n" + fecha(dia) + "\n")
		with open(directorio + fecha(dia) + ".txt", "w") as arch:
			for peli in pelis(dia):
				print(titulo(peli))
				arch.write(titulo(peli) + "\n")
				arch.write("	" + link(peli) + "\n")
				arch.write("\n")
	print("\nFIN")
	time.sleep(5)