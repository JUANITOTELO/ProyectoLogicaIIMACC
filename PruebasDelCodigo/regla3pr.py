import pr3Diccio
import os
from DPLL import DPLL
import string
from string import ascii_letters
from pr3Diccio import dibujar_solucion

"""----------Regla 3-----------"""
LcaminosIR = [i for i in string.ascii_lowercase]
letrasProposicionales = [i for i in string.ascii_uppercase]
LcaminosT = letrasProposicionales+LcaminosIR
R3 = [["S","X"],["~S","~X"]]

print(R3)

SR2 = DPLL(R3, {})

print(DPLL(R3, {}))
