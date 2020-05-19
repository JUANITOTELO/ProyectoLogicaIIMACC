from termcolor import colored,cprint
import pr3Diccio
import os
from DPLL import DPLL
import string
from string import ascii_letters
from pr3Diccio import dibujar_solucion
print("Se dibujara el mapa y se evaluara la regla 1")
LcaminosIR = [i for i in string.ascii_lowercase]
letrasProposicionales = [i for i in string.ascii_uppercase]
LcaminosT = letrasProposicionales+LcaminosIR

"""-------------Regla 1: Desde Sevilla a Santiago de Compostela------------"""
R1 = []

for i in range(25):
	R1.append(letrasProposicionales[i]+LcaminosIR[i])
	R1.append("~"+LcaminosIR[i]+"~"+letrasProposicionales[i])

print(R1)
SR1 = DPLL(R1, {})
print(DPLL(R1, {}))

dibujar_solucion(SR1[1], "mapacF0")

try:
    os.system("fim mapacF0.png")
    pass
except Exception as e:
    raise

"""-------------Regla 1: Desde Santiago de Compostela a Sevilla------------"""
R1I = []

for i in range(25):
	R1I.append(letrasProposicionales[i]+LcaminosIR[i])
	R1I.append("~"+letrasProposicionales[i]+"~"+LcaminosIR[i])

print(R1I)
SR1I = DPLL(R1I, {})
print(DPLL(R1I, {}))

dibujar_solucion(SR1I[1],"mapacF1")

try:
    os.system("fim mapacF1.png")
    pass
except Exception as e:
    raise( "nel Bro" )
