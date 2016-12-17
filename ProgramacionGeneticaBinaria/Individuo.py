import random
from operator import xor

##################### inicializacion del modulo ####################

# METODO  ----- Metodo para crear exprecion posfija FULL, GROW o HALF-AND-HALF
# setFun ----- Conjunto de funciones 
# numVar ----- Numero de variables 
# conInter --- Intervalo de constante
# Pvar  ------ probabilidad de escojer variables    
# Pconstan --- probabilidad de escojer constantes 
# PFun ------- probabilidad de escojer funciones    

metCrear = "FULL"
setFun = [ ['and','or','not','xor'], [2,2,1,2] ]
setVar = [chr(i) for i in xrange(97,97+25)] + [chr(i) for i in xrange(97-32,97-7)]
numVar = 3
#------- Probabilidades de cada uno de los signos ------------
PVar = 8
PConstan = 1
#-------------------------------------------------------------
print "metodo :"+ metCrear
print "sefFun :" + str(setFun)

class Individuo:
	

	def __init__(self, prof):
		self.gen=self.crearCadena(prof)
		self.calificacion=0
		self.error = 0


	################### funcion de adaptacion ############################
	def EMC(self,valE,resE):
		val = 0 
		for i in xrange(0,len(valE)): 
			val += ( float(self.evaluar(valE[i]) ) - float(resE[i]) )**2
		val /= float(len(valE)) 
		#print val
		self.error = val
		return val

	####################### Crear Arbol ##################################
	def crearCadena(self,prof):

			if metCrear == "FULL": 
				return self.full( prof )
			elif metCrear == "GROW": 
				return self.grow( prof )
			elif metCrear == "HalfaAndHalf": 
				return self.halfaAndHalf( prof )

	def full (self,prof):
		global numVar

		if (prof == 0):
			return [ setVar[ random.randint( 0, numVar-1 ) ] ]#Retorna una variable al azar
		else:
			fun = setFun[0][ random.randint( 0, len(setFun[0])-1 ) ]
			exp = [fun]
			i = setFun[0].index(fun)
			for i in xrange (0,setFun[1][i]):
				exp =  self.full(prof-1) + exp
			return exp

	def grow(self,prof):
		global numVar

		if (prof == 0):
			return [ setVar[ random.randint( 0, numVar-1 ) ] ]#Retorna una variable al azar
		else:
			if (random.random()<.5):
				fun = setFun[0][ random.randint( 0, len(setFun[0])-1 ) ]
				exp = [fun]
				i = setFun[0].index(fun)
				for i in xrange (0,setFun[1][i]):
					exp =  self.full(prof-1) + exp
				return exp
			else :
				return [ setVar[ random.randint( 0, numVar-1 ) ] ]

	def halfaAndHalf(self, prof):
		fun = setFun[0][ random.randint( 0, len(setFun[0])-1 ) ]
		inf = setFun[0].index(fun)
		exp = []
		for i in xrange (0,setFun[1][inf]):
			if i%2 == 0 :
				exp =  self.full(prof-1) + exp
			else :
				exp = self.grow(prof-1) + exp
		exp = exp +[fun]
		return exp

	###################### operadores #######################################

	def operador (self, op, X):
		global setFun
		global setVar

		if setFun[0][0] == op:
			return (X[0] and X[1])

		elif setFun[0][1] == op:
			return (X[0] or X[1])

		elif setFun[0][3] == op:
			return (xor( X[0],X[1]) )

		elif 'not' == op:
			if not X[0] :
				return 1
			else :
				return 0
	###################### Evaluacion #######################################

	def evaluar (self, val):
		pila = []
		pos = self.gen
		for i in xrange(0, len(pos)):
			if ( pos[i] in setVar ):
				pila.append(val[ setVar.index(pos[i]) ])
			else :
				indfun = setFun[0].index(pos[i])
				param = []
				for j in xrange(0,setFun[1][indfun]):
					param.insert(0, pila.pop() ) 
				res = self.operador(pos[i],param)
				pila.append(res)
		return pila.pop()


