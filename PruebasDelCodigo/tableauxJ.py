#-*-coding: utf-8-*-
from random import choice
from termcolor import colored,cprint
import string
from string import ascii_letters
##############################################################################
# Variables globales
##############################################################################
LcaminosIR = [i for i in string.ascii_lowercase]
letrasProposicionales = [i for i in string.ascii_uppercase]
ltotales = letrasProposicionales+LcaminosIR
# inicializa la lista de interpretaciones
listaInterpsVerdaderas = []
# inicializa la lista de hojas
listaHojas = []

##############################################################################
# Definición de objeto tree y funciones de árboles
##############################################################################
def Inorder(f):
	# Imprime una formula como cadena dada una formula como arbol
	# Input: tree, que es una formula de logica proposicional
	# Output: string de la formula
	if f.right == None:
		return f.label
	elif f.label == '~':
		return colored(f.label, "red", attrs =['bold']) + Inorder(f.right)
	else:
		if f.label == '&':
			return "(" + Inorder(f.left) + colored(f.label, "cyan", attrs =['bold']) + Inorder(f.right) + ")"
		if f.label == '>':
			return "(" + Inorder(f.left) + colored(f.label, "blue", attrs =['bold']) + Inorder(f.right) + ")"
		if f.label == '=':
			return "(" + Inorder(f.left) + colored(f.label, "green", attrs =['bold']) + Inorder(f.right) + ")"
		if f.label == '+':
			return "(" + Inorder(f.left) + colored(f.label, "magenta", attrs =['bold']) + Inorder(f.right) + ")"

class Tree(object):
	def __init__(self, label, left, right):
		self.left = left
		self.right = right
		self.label = label
	def get_label(self):
		return self.label
	def __str__(self):
		return "Tree({0},{1},{2})".format( self.label, self.left, self.right)


def string2Tree(A, ltotales):
	# Crea una formula como tree dada una formula
	# como cadena escrita en notacion polaca inversa
	# Input: A, lista de caracteres con una formula escrita en notacion polaca inversa
	#
	# Output: formula como tree
	conectivos = ['&','+','>','=']
	pila = []
	d = 0
	# ~ print(A)
	for c in A:
		# ~ e = A.find(A[d]+"'")
		# ~ print("A.find =",e,"c =",c, "d =",d, "A[d] =",A[d])
			# ~ print(Inorder(Tree(c+"'", None, None)),"entroo.")
		if c in ltotales:
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
	# print(colored(pila[-1],"red"))
	return pila[-1]

##############################################################################
# Definición de funciones de tableaux
##############################################################################

def imprime_hoja(H):
	cadena = "{"
	primero = True
	for f in H:
		if primero == True:
			primero = False
		else:
			cadena += ", "
		cadena += Inorder(f)
	return cadena + "}"

def par_complementario(l):
	# Esta función determina si una lista de solo literales
	# contiene un par complementario
	# Input: l, una lista de literales
	# Output: True/False
	#Entra de esta manera: lista=[Tree(q,None,None), Tree(-,None,Tree(p,None,None)),Tree(r,None,None)]
	#Hacer una lista de la forma[p,-p,q]
	mi_lista=[]
	for item in l:
		if item.label=='~':
			mi_lista.append('~'+item.right.label)
		else:
			mi_lista.append(item.label)
	#Comprobar si hay pares complementarios

	for elem in mi_lista:
		if elem[0]=='~':
			complementario=elem[1]
			if complementario in mi_lista:
				return True
		else:
			complementario='~'+elem[0]
			if complementario in mi_lista:
				return True
	return False

def es_literal(f):
	# Esta función determina si el árbol f es un literal
	# Input: f, una fórmula como árbol
	# Output: True/False
	#El input tiene esta forma: Tree(p,None,None)
	Conectivos = ['+','&','>','=']
	if f.label in Conectivos:
		return False
	elif f.label=='~':
		Conectivos.append('~')
		x = f.right
		if x.label in Conectivos:
			return False
		else:
			return True
	return True

def no_literales(l):
	# Esta función determina si una lista de fórmulas contiene
	# solo literales
	# Input: l, una lista de fórmulas como árboles
	# Output: None/f, tal que f no es literal
	for formula in l:
		if es_literal(formula) == False: #Si no es literal
			return formula

	return False



def alfa_beta(f):
	# ~ print(f.label)
	if f.label=='~':
		if f.right.label=='~': #Doble negación
			return 'a1'
		elif f.right.label=='+': #¬(A1oA2)
			return 'a3'
		elif f.right.label=='>': #¬(A1->A2)
			return 'a4'
		elif f.right.label=='&': #¬(B1∧B2)
			return 'b1'
		elif f.right.label=='=': #¬(B1<->B2)
			return 'b4'
		else:
			return 'HOJA'
	elif f.label=='&': #(A1 ∧ A2)
		return 'a2'
	elif f.label=='+': #(B1 o B2)
		return 'b2'
	elif f.label=='>': #(B! -> B2)
		return 'b3'
	elif f.label == '=': # (A1<->a2)
		return 'a5'
	else:
		return 'HOJA'

def clasifica_y_extiende(f,h):
	# clasifica una fórmula como alfa o beta y extiende listaHojas
	# de acuerdo a la regla respectiva
	# Input: f, una fórmula como árbol
	# Output: no tiene output, pues modifica la variable global listaHojas
	global listaHojas
	clasificacion = alfa_beta(f)
	if clasificacion=='HOJA':
		# ~ print("HOJA")
		listaHojas.remove([f])
		listaHojas.append(f)

	elif clasificacion == 'a1':
		print("a1")
		aux = [x for x in h]
		hijo = f.right.right
		aux.remove(f)
		aux.append(hijo)
		listaHojas.remove(h)
		listaHojas.append(aux)

	elif clasificacion=='a2':
		print("a2")
		aux = [x for x in h]
		hijo_izq=f.left
		hijo_der=f.right
		aux.remove(f)
		aux.append(hijo_der)
		aux.append(hijo_izq)
		listaHojas.remove(h)
		listaHojas.append(aux)

	elif clasificacion=='a3':
		aux = [x for x in h]
		hijo_izq=Tree('~',None,(f.right).left)
		hijo_der=Tree('~',None,(f.right).right)
		aux.remove(f)
		aux.append(hijo_der)
		aux.append(hijo_izq)
		listaHojas.remove(h)
		listaHojas.append(aux)
		print("a3")
		# for i in aux:
		# 	print(Inorder(i))

	elif clasificacion=='a4':
		print("a4")
		aux = [x for x in h]
		hijo_izq=(f.right).left
		hijo_der=Tree('~',None,(f.right).right)
		aux.remove(f)
		aux.append(hijo_der)
		aux.append(hijo_izq)
		listaHojas.remove(h)
		listaHojas.append(aux)

	elif clasificacion=='a5':
		print("a5")
		aux = [x for x in h]
		hiz = Tree('>',f.left,f.right)
		hde = Tree('>',f.right,f.left)
		aux.remove(f)
		aux.append(hiz)
		aux.append(hde)
		listaHojas.remove(h)
		listaHojas.append(aux)


	elif clasificacion=='b1':
		print("b1")
		aux = [x for x in h]
		hijo_izq=Tree('~',None,(f.right).left)
		hijo_der=Tree('~',None,(f.right).right)
		listaHojas.remove([f])
		listaHojas.append(hijo_izq)
		listaHojas.append(hijo_der)

	elif clasificacion=='b2':
		print("b2")
		aux = [x for x in h]
		hijo_izq=f.left
		hijo_der=f.right
		aux.remove(f)
		aux.append(hijo_der)
		aux.append(hijo_izq)
		listaHojas.remove(h)
		listaHojas.append(aux)

	elif clasificacion=='b3':
		print("b3")
		aux = [x for x in h]
		hijo_izq=Tree('~', None, f.left)
		hijo_der=f.right
		aux.remove(f)
		aux.append(hijo_izq)
		aux.append(hijo_der)
		listaHojas.remove(h)
		listaHojas.append(aux)

	elif clasificacion=='b4':
		print("b4")
		aux = [x for x in h]
		hiz = Tree('~', None,Tree('>',f.left,f.right))
		hde = Tree('~', None,Tree('>',f.right,f.left))
		aux.remove(f)
		aux.append(hijo_der)
		aux.append(hijo_izq)
		listaHojas.remove(h)
		listaHojas.append(aux)

def Tableaux(f):
	# Algoritmo de creacion de tableau a partir de lista_hojas
	# Imput: - f, una fórmula como string en notación polaca inversa
	# Output: interpretaciones: lista de listas de literales que hacen
	# verdadera a f
	global listaHojas
	global listaInterpsVerdaderas
	global ltotales

	A = string2Tree(f,ltotales)
	listaHojas = [[A]]
	while len(listaHojas)>0:
		for q in listaHojas:
			f = no_literales(q)
			if not f:
				if par_complementario(q):
					listaHojas.remove(q)
				else:
					listaInterpsVerdaderas.append(q)
					listaHojas.remove(q)
			else:
				clasifica_y_extiende(f,q)

	return listaInterpsVerdaderas

