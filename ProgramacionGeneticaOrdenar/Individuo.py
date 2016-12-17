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

metCrear = "GROW"
setFunSimple = [['+','-','/','*','==','!=','<=','>=','<','>','and','or','not','for','while','if','block2','block3','block4','block5','print'],[2,2,2,2,2,2,2,2,2,2,2,2,1,3,2,3,2,3,4,5,1]]
setFun = {
			"Aritmetic"   : [ ['+','-','/','*'], [2,2,2,2] ],
			"Comp"        : [ ['==','!=','<=','>=','<','>'],[2,2,2,2,2,2] ],
			"Logico"      : [ ['and','or','not'], [2,2,1]],
			"Iterativo"   : [ ['for','while'],[3,2] ],
			"Condicional" : [ ['if'] ,[3] ],
			"MulBlock"    : [ ['block2','block3','block4','block5'],[2,3,4,5] ],
			#"List"        : [ ['append','sort','[]'],[2,1,2] ],
			"Salida"     : [ ['print'],[1] ],
			#"Asignacion"  : [ ['=' ],[2] ], 
}

setFunBlock = ['for','while','if',"MulBlock"]  

setFunNom = [ 
					"Aritmetic", 
					"Comp", 
					"Logico", 
					"Iterativo", 
					"Condicional", 
					"MulBlock",
					#"List",
					"Salida",
					#"Asignacion"
				]

#setFun = [ ['and','or','not','+','-','/','*','<','>','==','!=','for'], [2,2,1,2,2,2,2,2,2,2,2,3], ]
setVar = [chr(i) for i in xrange(97,97+25)] + [chr(i) for i in xrange(97-32,97-7)]
numVar = 3
setVarCon = ['Cons'+chr(i) for i in xrange(97,97+25)] + [chr(i) for i in xrange(97-32,97-7)]
numVarCon = 3
#------- Probabilidades de cada uno de los signos ------------
PVar = 8
PConstan = 1
#-------------------------------------------------------------

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
			elif metCrear == "halfaAndHalf": 
				return self.halfaAndHalf( prof )
	"""			
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
	"""		
	def grow(self,prof):
		global numVar

		if (prof == 0):
			if (random.random()<.8):
				return [ setVar[ random.randint( 0, numVar-1 ) ] ]#Retorna una variable al azar
			else :
				return [ setVarCon[ random.randint( 0, numVarCon-1 ) ] ]
		else:
			if (random.random()<.8):
				funCla = setFunNom[ random.randint( 0, len(setFunNom)-1 ) ]
				fun = setFun[funCla][0][ random.randint( 0, len(setFun[funCla][0])-1 ) ]
				exp = [fun]
				r = setFun[funCla][0].index(fun)

				if fun in setFunBlock:
					for i in xrange (0,setFun[funCla][1][r]):
						exp =  [self.grow(prof-1)] + exp
					exp = [exp]
				else :
					for i in xrange (0,setFun[funCla][1][r]):
						exp =  self.grow(prof-1) + exp
				return exp
			else :
				if (random.random()<.8):
					return [ setVar[ random.randint( 0, numVar-1 ) ] ]#Retorna una variable al azar
				else :
					return [ setVarCon[ random.randint( 0, numVarCon-1 ) ] ]
	"""			
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
	"""	
	###################### operadores #######################################

	def operador (self, op, X):
		global setFun
		global setVar
		########### logicos ############
		if 'and' == op:
			return ( X[0]  and  X[1]) 
		elif 'or' == op:
			return ( X[0] or X[1] ) 
		elif 'not' == op:
			not X[0] 
	   	######### Aritmeticos ###########
		elif '+' == op:
			return X[0]+X[1]
		elif '-' == op:
			return X[0]-X[1]
		elif '/' == op:
			if X[1] == 0.0 and X[1] == False :
				return 0.0
			else :
				return X[0]/X[1]
		elif '*' == op:
			return X[0]*X[1]  
		############ condicionales ############
		elif '<' == op:
			return X[0]<X[1]  
		elif '>' == op:
			return X[0]>X[1]  
		elif '==' == op:
			return X[0]==X[1]  
		elif '!=' == op:
			return X[0]!=X[1]
		elif '>=' == op:
			return X[0]>=X[1]
		elif '<=' == op:
			return X[0]<=X[1]  
		########## Iterativo ############
		#elif 'for' == ap:




	###################### Evaluacion #######################################

	def evaluar (self, val):
		pila = []
		pos = self.gen
		for i in xrange(0, len(pos)):
			print "fdgfd"
			print pos[i]
			if str(type(pos[i])) == "<type 'list'>":
				print pos[i].pop()
				if ( pos[i] in setVar ):
					pila.append(val[ setVar.index(pos[i]) ])
				else :
					indfun = setFun[0].index(pos[i])
					param = []
					for j in xrange(0,setFun[1][indfun]):
						param.insert(0, pila.pop() ) 
					res = self.operador(pos[i],param)
					pila.append(res)
			else :
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


prueba = Individuo(5)
print prueba.gen

prueba.evaluar([5,4,4])