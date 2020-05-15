import pr3Diccio
import os
from DPLL import DPLL
import string
from string import ascii_letters
from pr3Diccio import dibujar_solucion

"""----------Regla 2-----------"""
LcaminosIR = [i for i in string.ascii_lowercase]
letrasProposicionales = [i for i in string.ascii_uppercase]
LcaminosT = letrasProposicionales+LcaminosIR
R2 = [["~V","~U"],["~O","~N"],["~L","~K"],["~C","~B"],["~C","~A"],["~B","~A"]]

print(R2)

SR2 = DPLL(R2, {})

print(DPLL(R2, {}))
