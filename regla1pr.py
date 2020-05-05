from termcolor import colored,cprint
import tableauxJ as T
class Tree:
	def __init__(self,l,iz,dr):
		self.label = l
		self.left = iz
		self.right = dr
		
	def __str__(self):
		return "Tree({},{},{})".format(self.label,self.left,self.right)

Nf = 25 # Numero de filas
Nc = 1 # Numero de columnas
aR1 = "" # Inicializa la regla
c = 0 # Contador de &
LcaminosD = [chr(i) for i in range(65, 65 + Nf*Nc)] #Letras de los caminos A
LcaminosIR = [chr(i)+"'" for i in range(65, 65 + Nf*Nc)] #Letras de los caminos A'
LcaminosIR1 = ["'"+chr(i) for i in range(65, 65 + Nf*Nc)] #Letras de los caminos inversos
LcaminosT = LcaminosD + LcaminosIR

for i in range(len(LcaminosD)):
	aR1 += "="+LcaminosD[i]+"~"+LcaminosIR1[i]
	c+=1

R1 = aR1[::-1]+"&"*(c-1)
print ("Formula en notación polaca inversa:\n",colored(R1,"yellow"),"\n")

def Inorder(f):
    # Imprime una formula como cadena dada una formula como arbol
    # Input: tree, que es una formula de logica proposicional
    # Output: string de la formula
	if f.right == None:
		return f.label
	elif f.label == '~':
		return f.label + Inorder(f.right)
	else:
		return (Inorder(f.left) + f.label + Inorder(f.right))

def string2Tree(A, letrasProposicionales):
	# Crea una formula como tree dada una formula
	# como cadena escrita en notacion polaca inversa
	# Input: A, lista de caracteres con una formula escrita en notacion polaca inversa
	#
	# Output: formula como tree
	conectivos = ['&','o','>','=']
	pila = []
	d = 0
	for c in A:
		e = A.find(c+"'")
		# ~ print("A.find =",e,c, "d =",d,A[d])
		if (e == d):
			pila.append(Tree(c+"'", None, None))
			# ~ print(Inorder(Tree(c+"'", None, None)),"entroo.")
		elif c in letrasProposicionales:
			pila.append(Tree(c, None, None))
			# ~ print(Inorder(Tree(c, None, None)), "tambien entroo.")
		elif c == '~':
			formulaAux = Tree(c, None, pila[-1])
			del pila[-1]
			pila.append(formulaAux)
		elif c in conectivos:
			formulaAux = Tree(c, pila[-1], pila[-2])
			del pila[-1]
			del pila[-1]
			pila.append(formulaAux)
		# ~ print(pila[0].label)
		d += 1
	# ~ print(pila[-1])
	return pila[-1]


R1S = string2Tree(R1, LcaminosT)
print("Formula en notación normal:\n",Inorder(R1S))
ta = T.Tableaux(R1)
if len(ta) == 0:
	print('La fórmula es insatisfacible')
else:
	print('La fórmula es satisfacible.')
	print('Las hojas abiertas del tableaux son:')
	for l in ta:
		print(T.imprime_hoja(l))
