import random

##################### inicializacion del modulo ####################

# METODO  ----- Metodo para crear exprecion posfija FULL, GROW o HALF-AND-HALF
# setFun ----- Conjunto de funciones 
# numVar ----- Numero de variables 
# conInter --- Intervalo de constante
# Pvar  ------ probabilidad de escojer variables    
# Pconstan --- probabilidad de escojer constantes 
# PFun ------- probabilidad de escojer funciones    

metCrear = "FULL"
setFun = [ ['and','or','not'], [2,2,1] ]
setVar = [chr(i) for i in xrange(97,97+25)] + [chr(i) for i in xrange(97-32,97-7)]
numVar = 3
#------- Probabilidades de cada uno de los signos ------------
PVar = 8
PConstan = 1
#-------------------------------------------------------------

class Individuo:
	

	gen=[]
	calificacion=0
	error = 0
	def __init__(self, prof):
		self.gen=self.crearCadena(prof)


	################### funcion de adaptacion ############################
	def error(self,valE,resE):
		val = 0 
		for i in xrange(0,len(valE)): 
			val += ( float(self.evaluar(valE[i]) ) - float(resE[i]) )**2
		val /= len(valE) 
		#print val
		self.error = val
		return val

	####################### Crear Arbol ##################################
	def crearCadena(self,prof):
			if metCrear == "FULL": 
				return self.full( prof )

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
	###################### operadores #######################################

	def operador (self, op, X):
		global setFun
		global setVar

		if setFun[0][0] == op:
			return (X[0] and X[1])

		elif setFun[0][1] == op:
			return (X[0] or X[1])

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


