from termcolor import colored,cprint
import pr3Diccio
import os
from DPLL import DPLL
import string
from string import ascii_letters
from pr3Diccio import dibujar_solucion

RT = [['~A','D'],['~D','A'],['~B','E'],['~E','B'],['~C','F'],['~F','C'],['~D','G'],['~G','D'],['~E','H'],['~H','E'],['~F','I'],['~I','F'],['~G','~J'],['J','G'],['~H','K','L'],['~K','H'],['~L','H'],['~I','M'],['~M','I'],['J','N','O'],['~N','~J'],['~O','J'],['~K','P'],['~P','K'],['~L','Q'],['~Q','L'],['~M','R'],['~R','M'],['~N','S'],['~S','N'],['~O','T'],['~T','O'],['~P','~J'],['J','P'],['~Q','U','V'],['~U','Q'],['~V','Q'],['~R','W'],['~W','R'],['~T','X'],['~X','T'],['~U','Y'],['~Y','U'],['~W','T'],['~T','W'],['~Y','N','O'],['~N','Y'],['~O','Y'],['~A','~B'],['~A','~C'],['~B','~C'],['~K','~L'],['~N','~O'],['~U','~V'],['S','X'],['~S','~X']]

SR4 = DPLL(RT, {})
print(SR4)

dibujar_solucion(SR4[1], "mapacF4")

try:
    os.system("fim mapacF4.png")
    os.system("fim mapacF4I.png")
    os.system("fim mapacF4T.png")
    pass
except Exception as e:
    raise

