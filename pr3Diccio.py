#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 14:32:19 2020

@author: juanitotelo
"""
from PIL import Image,ImageDraw
import random
import string
from string import ascii_letters
from termcolor import colored,cprint
Nf = 25 # Numero de filas
Nc = 1 # Numero de columnas
LcaminosD = [chr(i) for i in range(65, 65 + Nf*Nc)] #Letras de los caminos
LcaminosI = [chr(i)+"'" for i in range(65, 65 + Nf*Nc)] #Letras de los caminos inversos
L = [i for i in string.ascii_lowercase]
LT = L + LcaminosD
sevilla = (427,475)
merida = (413,368)
cordoba = (484,429)
jaen = (563,434)
caceres = (394,319)
ciudad_real = (545,361)
albacete = (648,367)
salamanca = (440,222)
toledo = (529,297)
cuenca = (638,296)
zamora = (437,176)
avila = (485,241)
madrid = (547,250)
soria = (607,171)
orense = (316,118)
leon = (434,94)
segovia = (525,194)
burgos = (550,106)
lugo = (350,58)
valladolid = (486,167)
santiago_de_sompostela = (294,62)

lCiudades = [sevilla,merida,cordoba,jaen,
			caceres,ciudad_real,albacete,
			salamanca,toledo,cuenca,zamora,
			avila,madrid,soria,orense,leon,
			segovia,burgos,lugo,valladolid,
			santiago_de_sompostela]

NumeroDlCiudades= {}

for i in range(len(lCiudades)):
	NumeroDlCiudades[i] = lCiudades[i]
"""
0 Sevilla
1 Merida
2 Cordoba
3 Jaen
4 Caceres
5 Ciudad Real
6 Albacete
7 Salamanca
8 Toledo
9 Cuenca
10 Zamora
11 Avila
12 Madrid
13 Soria
14 Orense
15 Leon
16 Segovia
17 Burgos
18 Lugo
19 Valladolid
20 Santiago de Compostela
"""
PcaminosD = [] # Ubicación de caminos
DLCaminos={} # Diccionario con las letras de los caminos

# Se agregan todos los caminos al diccionario
DLCaminos[LcaminosD[0]] = [NumeroDlCiudades[0],NumeroDlCiudades[1]]
DLCaminos[LcaminosD[1]] = [NumeroDlCiudades[0],NumeroDlCiudades[2]]
DLCaminos[LcaminosD[2]] = [NumeroDlCiudades[0],NumeroDlCiudades[3]]
DLCaminos[LcaminosD[3]] = [NumeroDlCiudades[1],NumeroDlCiudades[4]]
DLCaminos[LcaminosD[4]] = [NumeroDlCiudades[2],NumeroDlCiudades[5]]
DLCaminos[LcaminosD[5]] = [NumeroDlCiudades[3],NumeroDlCiudades[6]]
DLCaminos[LcaminosD[6]] = [NumeroDlCiudades[4],NumeroDlCiudades[7]]
DLCaminos[LcaminosD[7]] = [NumeroDlCiudades[5],NumeroDlCiudades[8]]
DLCaminos[LcaminosD[8]] = [NumeroDlCiudades[6],NumeroDlCiudades[9]]
DLCaminos[LcaminosD[9]] = [NumeroDlCiudades[7],NumeroDlCiudades[10]]
DLCaminos[LcaminosD[10]] = [NumeroDlCiudades[8],NumeroDlCiudades[11]]
DLCaminos[LcaminosD[11]] = [NumeroDlCiudades[8],NumeroDlCiudades[12]]
DLCaminos[LcaminosD[12]] = [NumeroDlCiudades[9],NumeroDlCiudades[13]]
DLCaminos[LcaminosD[13]] = [NumeroDlCiudades[10],NumeroDlCiudades[14]]
DLCaminos[LcaminosD[14]] = [NumeroDlCiudades[10],NumeroDlCiudades[15]]
DLCaminos[LcaminosD[15]] = [NumeroDlCiudades[11],NumeroDlCiudades[7]]
DLCaminos[LcaminosD[16]] = [NumeroDlCiudades[12],NumeroDlCiudades[16]]
DLCaminos[LcaminosD[17]] = [NumeroDlCiudades[13],NumeroDlCiudades[17]]
DLCaminos[LcaminosD[18]] = [NumeroDlCiudades[14],NumeroDlCiudades[20]]
DLCaminos[LcaminosD[19]] = [NumeroDlCiudades[15],NumeroDlCiudades[18]]
DLCaminos[LcaminosD[20]] = [NumeroDlCiudades[16],NumeroDlCiudades[19]]
DLCaminos[LcaminosD[21]] = [NumeroDlCiudades[16],NumeroDlCiudades[17]]
DLCaminos[LcaminosD[22]] = [NumeroDlCiudades[17],NumeroDlCiudades[15]]
DLCaminos[LcaminosD[23]] = [NumeroDlCiudades[18],NumeroDlCiudades[20]]
DLCaminos[LcaminosD[24]] = [NumeroDlCiudades[19],NumeroDlCiudades[10]]

def dibujar_flecha(I,C):
	# ~Coordenadas de ciudades dadas en tuplas
	global LcaminosD
	global LcaminosI
	global L
	global lCiudades
	global NumeroDlCiudades
	global PcaminosD
	global DLCaminos
	mapa=Image.open(I)
	draw = ImageDraw.Draw(mapa)
	nR = random.randint(10,255)

	if(C in LcaminosD):
		draw.line(DLCaminos[C], fill=0,width=6)
		draw.ellipse([(DLCaminos[C][1][0]-15,DLCaminos[C][1][1]-15), (DLCaminos[C][1][0]+15,DLCaminos[C][1][1]+15)], fill = (0,0,0))
		draw.ellipse([(DLCaminos[C][1][0]-8,DLCaminos[C][1][1]-8), (DLCaminos[C][1][0]+8,DLCaminos[C][1][1]+8)], fill = (nR,nR,nR))
	elif(C in LcaminosI or C in L):
		n = L.index(C)
		C = LcaminosI[n]
		draw.line(DLCaminos[C[0]], fill=(255,255,255),width=6)
		draw.ellipse([(DLCaminos[C[0]][0][0]-15,DLCaminos[C[0]][0][1]-15), (DLCaminos[C[0]][0][0]+15,DLCaminos[C[0]][0][1]+15)], fill = (255,255,255))
		draw.ellipse([(DLCaminos[C[0]][0][0]-8,DLCaminos[C[0]][0][1]-8), (DLCaminos[C[0]][0][0]+8,DLCaminos[C[0]][0][1]+8)], fill = (nR,nR,nR))
	else:
		print(colred("LOL! esto no es un camino.", "red", attrs =['bold', 'blink']))

	text_img = Image.new('RGB', (1000,686), (0, 0, 0, 0))
	text_img.paste(mapa,(0,0))
	return text_img

def dibujar_solucion(diccionario, nombreImagen):
	MP = []
	MPI = []
	for i in diccionario:
		if(diccionario[i] == 1 and i in LT):
			MP.append(i)
		else:
			MPI.append(i)
	if (MP):
		f1 = dibujar_flecha("Provinces_of_Spain-2.png",MP[0])
		print(colored("Camino dibujado.","green", attrs =['bold']))
		MP.pop(0)
		f1.save("{}.png".format(nombreImagen),format="png")
		for i in MP:
			I2 = dibujar_flecha("{}.png".format(nombreImagen), i)
			I2.save("{}.png".format(nombreImagen),format="png")
			print(colored("Camino dibujado.","green", attrs =['bold']))
	
	else:
		print(colored("No hay valores verdaderos.","red", attrs =['bold','blink']))
	MPT = MPI+MP
	if (MPI):
		f1 = dibujar_flecha("Provinces_of_Spain-2.png",MPI[0])
		print(colored("Camino dibujado.","green", attrs =['bold']))
		MPI.pop(0)
		f1.save("{}I.png".format(nombreImagen),format="png")
		for i in MPI:
			I2 = dibujar_flecha("{}I.png".format(nombreImagen), i)
			I2.save("{}I.png".format(nombreImagen),format="png")
			print(colored("Camino dibujado.","green", attrs =['bold']))
	
	else:
		print(colored("No hay valores verdaderos.","red", attrs =['bold','blink']))
		
	if (MPT):
		f1 = dibujar_flecha("Provinces_of_Spain-2.png",MPT[0])
		print(colored("Camino dibujado.","green", attrs =['bold']))
		MPI.pop(0)
		f1.save("{}T.png".format(nombreImagen),format="png")
		for i in MPT:
			I2 = dibujar_flecha("{}T.png".format(nombreImagen), i)
			I2.save("{}T.png".format(nombreImagen),format="png")
			print(colored("Camino dibujado.","green", attrs =['bold']))
	
	else:
		print(colored("No hay valores verdaderos.","red", attrs =['bold','blink']))
