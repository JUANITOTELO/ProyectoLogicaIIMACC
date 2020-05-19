import pr3Diccio
import os
from \código\DPLL import DPLL
import string
from string import ascii_letters
from \código\pr3Diccio import dibujar_solucion

"""----------Regla 3-----------"""
LcaminosIR = [i for i in string.ascii_lowercase]
letrasProposicionales = [i for i in string.ascii_uppercase]
LcaminosT = letrasProposicionales+LcaminosIR

R1 = []
for i in range(25):
	R1.append([letrasProposicionales[i]]+[LcaminosIR[i]])
	R1.append(["~"+letrasProposicionales[i]]+["~"+LcaminosIR[i]])

R2 = [["~V","~U"],["~O","~N"],["~L","~K"],["~C","~B"],["~C","~A"],["~B","~A"]]
R3 = [["S","X"],["~S","~X"]]
RAS = R1+R2+R3

print(RAS)
SRAS = DPLL(RAS, {})
print(DPLL(RAS, {}))

dibujar_solucion(SRAS[1], "mapacF3")

try:
    os.system("fim mapacF3.png")
    os.system("fim mapacF3I.png")
    os.system("fim mapacF3T.png")
    pass
except Exception as e:
    raise


