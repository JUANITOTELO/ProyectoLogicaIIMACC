from termcolor import colored,cprint
import pr3Diccio
import os
from DPLL import DPLL
import string
from string import ascii_letters
from pr3Diccio import dibujar_solucion
# ~ Se crean las reglas normales e inversas
RT = [['~A','D'],['~D','A'],['~B','E'],['~E','B'],['~C','F'],['~F','C'],['~D','G'],['~G','D'],['~E','H'],['~H','E'],['~F','I'],['~I','F'],['~G','~J'],['J','G'],['~H','K','L'],['~K','H'],['~L','H'],['~I','M'],['~M','I'],['J','N','O'],['~N','~J'],['~O','J'],['~K','P'],['~P','K'],['~L','Q'],['~Q','L'],['~M','R'],['~R','M'],['~N','S'],['~S','N'],['~O','T'],['~T','O'],['~P','~J'],['J','P'],['~Q','U','V'],['~U','Q'],['~V','Q'],['~R','W'],['~W','R'],['~T','X'],['~X','T'],['~U','Y'],['~Y','U'],['~W','T'],['~T','W'],['~Y','N','O'],['~N','Y'],['~O','Y'],['~A','~B'],['~A','~C'],['~B','~C'],['~K','~L'],['~N','~O'],['~U','~V'],['S','X'],['~S','~X']]

RTI = [[]] #esta es la inversa 
for i in range(len(RT)):
	for j in range(len(RT[i])):
		RTI[i].append(RT[i][j].lower())
	RTI.append([])

RTI.pop(len(RT))
# ~ ------------------------------------
# ~ Se ejecuta el código DPLL para generar las soluciónes
SR4 = DPLL(RT, {})
SR5 = DPLL(RTI, {})
print(SR4)
# ~ ------------------------------------
# ~ Se ejecuta el código para dibujar las soluciones en varios mapas
dibujar_solucion(SR4[1], "mapacF4")
# ~ ------------------------------------
# ~ Se abren las imagenes con una herramienta en linux ubuntu llamada "fim"
try:
    os.system("fim mapacF4.png")
    # ~ os.system("fim mapacF4I.png")
    # ~ os.system("fim mapacF4T.png")
    pass
except Exception as e:
    raise

print(SR5)

dibujar_solucion(SR5[1], "mapacF5")

try:
    os.system("fim mapacF5.png")
    # ~ os.system("fim mapacF5I.png")
    # ~ os.system("fim mapacF5T.png")
    pass
except Exception as e:
    raise
# ~ -----------------------------------
