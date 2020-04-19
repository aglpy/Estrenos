#******************************************************************************
#Guarda en una tabla de DynamoDB de AWS a través de lambda los estrenos
#con las fechas y los links de filmaffinity a estas peliculas
#@angalaagl
#https://github.com/aglpy
#https://anaconda.org/angala
#******************************************************************************

import urllib.request
from bs4 import BeautifulSoup
import boto3
import time

ddb = boto3.client('dynamodb')
link_estrenos = "https://www.filmaffinity.com/es/rdcat.php?id=upc_th_es" #Pagina donde están los estrenos de España
link_filmaffinity = "https://www.filmaffinity.com" #Usado para obtener el link completo de cada peli

def dias(body): #Devuelve un array con los dias disponibles en body
	return body.find_all("div", attrs={"id":"main-wrapper-rdcat"})

def fecha(dia): #Devuelve la fecha del dia
	return dia.find("div", attrs={"class":"rdate-cat"})["id"]

def pelis(dia): #Devuelve un array con todas las pelis en el dia dado
	return dia.find_all("div", attrs={"class":"top-movie"})

def titulo(peli): #Devuelve el titulo de la peli
	return peli.find("div", attrs={"class":"mc-right"}).find("h3").find("a")["title"]
	
def link(peli): #Devuelve el link completo de la peli
	return link_filmaffinity +\
	peli.find("div", attrs={"class":"mc-right"}).find("h3").find("a")["href"]

def lambda_handler(event, context):
	pag = urllib.request.urlopen(link_estrenos) #Obtenemos el html
	body = BeautifulSoup(pag) #Creamos el parseable

	for dia in dias(body): #Para cada dia que aparezca en la pagina
		for peli in pelis(dia): #Para cada peli en ese dia
			ddb.put_item(TableName='trailers', 
						 Item={'date':{'S':fecha(dia)}, 
							   'title':{'S':titulo(peli)},
						 	   'link':{'S':link(peli)}
						 })
			time.sleep(1)