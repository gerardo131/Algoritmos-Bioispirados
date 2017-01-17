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

setFunBlock = ['for','while','if','block2','block3','block4','block5']  

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
setVarCon = ['Cons'+chr(i) for i in xrange(97,97+25)] 
numVarCon = 3
#------- Probabilidades de cada uno de los signos ------------
PVar = 8
PConstan = 1
#-------------------------------------------------------------

class Individuo:
	

	def __init__(self, prof):
		self.gen=self.crearCadena(prof)
		self.genRES = self.gen[:]
		self.calificacion=0
		self.error = 0
		self.valCon=[random.randint( 0, 800000 ) for i in xrange(0,numVarCon)]
		self.resultado = []


	################### funcion de adaptacion ############################
	def EMC(self,valE,resE):
		val = 0 
		for i in xrange(0,len(valE)): 
			res = self.evaluarGen(valE[i])
			if res == None:
				res = []
			#print res
			if len(res) < len(resE[i]):
				for j in xrange(0,len(res)) :
					if res[j] == resE[i][j]:
						val += 1.0
			else :
				for j in xrange(0,len(resE[i])) :
					if res[j] == resE[i][j]:
						val += 1.0
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
					exp = exp
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

	def operador (self,val, op, X):
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

		elif 'for' == op:
			#print "Entro al for"
			if self.evaluar(val, X[0])<self.evaluar(val, X[1]):
				for i in xrange(self.evaluar(val, X[0]),self.evaluar(val, X[1]) ):
					self.evaluar(val, X[2])
			else :
				for i in xrange(self.evaluar(val, X[0]),self.evaluar(val, X[1]),-1 ):
					self.evaluar(val, X[2])

		elif 'while' == op:
			conStop = 10
			#print "Entro al while"
			while self.evaluar(val, X[0] ) and conStop:
				self.evaluar(val, X[1])
				conStop-=1
		elif 'if ' == op:
			#print "Entro al if"
			if self.evaluar(val, X[0]):
				self.evaluar(val,  X[1])
			else:
				self.evaluar(val, X[2])
		elif 'print' ==  op:
			self.resultado.append(X[0])

		######### Multiblock ######
		elif 'block2' == op :
			self.evaluar(val,  X[0])
			self.evaluar(val,  X[1])
		elif 'block3' == op :
			self.evaluar(val,  X[0])
			self.evaluar(val,  X[1])
			self.evaluar(val,  X[2])
		elif 'block4' == op :
			self.evaluar(val,  X[0])
			self.evaluar(val,  X[1])
			self.evaluar(val,  X[2])
			self.evaluar(val,  X[3])
		elif 'block5' == op :
			self.evaluar(val,  X[0])
			self.evaluar(val,  X[1])
			self.evaluar(val,  X[2])
			self.evaluar(val,  X[3])
			self.evaluar(val,  X[4])





	###################### Evaluacion #######################################

	def evaluar (self, val,pos):
		pila = []
		
		for i in xrange(0, len(pos)):
			#print "fdgfd"
			#print pos[i]

			if ( pos[i] in setVar   ):
				pila.append(val[ setVar.index(pos[i]) ])

			elif str(type(pos[i])) == "<type 'list'>": 
				pila.append(pos[i])
			elif pos[i] in setVarCon:
				pila.append( self.valCon[setVarCon.index(pos[i])] )

			else :
				indfun = setFunSimple[0].index(pos[i])
				param = []
				for j in xrange(0,setFunSimple[1][indfun]):
					param.insert(0, pila.pop() ) 
				res = self.operador(val,pos[i],param)
				pila.append(res)
		return pila.pop()

	def evaluarGen(self, val):
		try:
			self.evaluar(val,self.gen)
			if  self.resultado == None:
				return []
			else:
				return self.resultado
		except Exception as inst:
			self.resultado=[]
			#print  inst
"""
prueba = Individuo(5)
res = prueba.evaluarGen([5,4,4])
print "el resultado es "
print res
"""