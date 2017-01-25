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
setFunSimple = [['+','-','/','*','==','!=','<=','>=','<','>','and','or','not','for','while','if','block2','block3','block4','block5','print','None'],[2,2,2,2,2,2,2,2,2,2,2,2,1,3,2,3,2,3,4,5,1,0]]
setFun = {
			"Ari"   : [ ['+','-','/','*'], [2,2,2,2],[[['R','Ari'],['R','Ari'] ],[['R','Ari'],['R','Ari'] ],[['R','Ari'],['R','Ari'] ],[['R','Ari'],['R','Ari'] ] ]],
			"Com"   : [ ['==','!=','<=','>=','<','>'],[2,2,2,2,2,2],[[['R','Ari'],['R','Ari'] ],[['R','Ari'],['R','Ari'] ],[['R','Ari'],['R','Ari'] ],[['R','Ari'],['R','Ari'] ],[['R','Ari'],['R','Ari'] ],[['R','Ari'],['R','Ari'] ] ]],
			"Log"   : [ ['and','or','not'], [2,2,1],[ [['B','Log','Com'],['B','Log','Com']], [['B','Log','Com'],['B','Log','Com']], [['B','Log','Com']] ]],
			"Ite"   : [ ['for','while'],[3,2],[ [['R','Ari'],['R','Ari'],['Ite','Con','MuB','Sal']], [['Log'],['Ite','Con','MuB','Sal']] ]],
			"Con"   : [ ['if'] ,[3],[[ ['Log'], ['Ite','Con','MuB','Sal'], ['Ite','Con','MuB','Sal'] ]] ],
			"MuB"   : [ ['block2','block3','block4','block5'],[2,3,4,5],[ [['Ite','Con','MuB','Sal'],['Ite','Con','MuB','Sal']], [['Ite','Con','MuB','Sal'],['Ite','Con','MuB','Sal'],['Ite','Con','MuB','Sal']], [['Ite','Con','MuB','Sal'],['Ite','Con','MuB','Sal'],['Ite','Con','MuB','Sal'],['Ite','Con','MuB','Sal']],[['Ite','Con','MuB','Sal'],['Ite','Con','MuB','Sal'],['Ite','Con','MuB','Sal'],['Ite','Con','MuB','Sal'],['Ite','Con','MuB','Sal']] ] ],
			#"List"        : [ ['append','sort','[]'],[2,1,2] ],
			"Sal"   : [ ['print'],[1],[[['R']]] ],
			"Bak"   : [ ['None'],[0],[]] 
			#"Asignacion"  : [ ['=' ],[2] ], 
}

setFunBlock = ['for','while','if','block2','block3','block4','block5']  

setFunNom = [ 
					"Ari", 
					"Com", 
					"Log", 
					"Ite", 
					"Con", 
					"MuB",
					#"List",
					"Sal",
					"Bak"
					#"Asignacion"
				]

#setFun = [ ['and','or','not','+','-','/','*','<','>','==','!=','for'], [2,2,1,2,2,2,2,2,2,2,2,3], ]
numVar = 10
numVarCon = 3
numVarConB = 3

setVar = [chr(i) for i in xrange(97,97+numVar)] 
setVarCon = ['Cons'+chr(i) for i in xrange(97,97+numVarCon)] 
setVarConB = ['ConsB'+chr(i) for i in xrange(97,97+numVarCon)] 
valCon=[random.randint( 0,20 ) for i in xrange(0,numVarCon)]
valConB = [random.choice([True, False]) for i in xrange(0,numVarCon)]

setFunIn={
			'Bin'  : setFun['Com'][0]+setFun['Log'][0]+setVarConB,
			'Block': setFun['Ite'][0]+setFun['Con'][0]+setFun['MuB'][0]+setFun['Sal'][0]+setFun['Bak'][0],
			'Arit' : setFun['Ari'][0]+ setVar+setVarCon+['for'+chr(i) for i in xrange(0,100)] 
		}


#------- Probabilidades de cada uno de los signos ------------
PVar = 8
PConstan = 1
#-------------------------------------------------------------

class Individuo:
	

	def __init__(self, prof):
		self.Nfor = 0
		self.forVal = []
		self.gen = self.crearCadena(prof)
		self.calificacion = 0
		self.error = 0
		self.resultado = []
		


	################### funcion de adaptacion ############################
	def EMC(self,valE,resE):
		val = 0.0 
		for i in xrange(0,len(valE)): 
			parVal = 0.0
			res = self.evaluarGen(valE[i])
			#print res
			for j in xrange(0,len(resE[i])) :
				if j<len(res):
					if res[j] != resE[i][j]:
						parVal += 1.0
				else:
					parVal += 3.0  
			val += float(parVal)/float(len(resE[i]))

		val = (val**2)/float(len(valE)) 
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
	def grow(self,prof,Tipo=['Ite','Con','MuB','Sal']):
		global setVarCon
		if (prof == 0):
			##### Real ######
			if 'R' in Tipo:
				if (random.random()<.8):
					return [ setVar[ random.randint( 0, len(setVar)-1 ) ] ]#Retorna una variable al azar
				else :
					return [ setVarCon[ random.randint( 0, len(setVarCon)-1 ) ] ]
			##### Binaria ####
			elif 'Log' in Tipo:
				return [ setVarConB[ random.randint( 0, len(setVarConB)-1 ) ] ]
			##### Bloque  ####
			elif 'MuB' in Tipo:
				return ['None']
		else:
			if (random.random()<.9 and not('R'in Tipo and len(Tipo)==1) and not('R'in Tipo and len(Tipo)==1) ):
				TipoC = Tipo[:]
				if 'R' in TipoC  :
					TipoC.remove('R')
				elif 'B' in TipoC:
					TipoC.remove('B')

				funCla = TipoC[ random.randint( 0, len(TipoC)-1 ) ]
				Nfun = random.randint( 0, len(setFun[funCla][0])-1 )
				fun = setFun[funCla][0][Nfun]
				exp = [fun]
				r = setFun[funCla][0].index(fun)
				#print fun
				#print setFun[funCla][2][Nfun][0]
				if fun in setFunBlock:
					if fun == 'for':
						exp =  [self.grow(prof-1,setFun[funCla][2][Nfun][0])] + exp
						self.Nfor +=1 
						setVarCon.append('for'+str(self.Nfor))
						exp =  [self.grow(prof-1,setFun[funCla][2][Nfun][1])] + exp
						exp =  [self.grow(prof-1,setFun[funCla][2][Nfun][2])] + exp
						for i in xrange(0,self.Nfor):
							setVarCon.pop()
						self.Nfor =0
						exp = exp
					else:
						for i in xrange (0,setFun[funCla][1][r]):
							exp =  [self.grow(prof-1,setFun[funCla][2][Nfun][i])] + exp
						exp = exp
				else :
					for i in xrange (0,setFun[funCla][1][r]):
						a = self.grow(prof-1,setFun[funCla][2][Nfun][i])
						#print  a
						exp =  a + exp
				#print exp
				return exp
			else :
				##### Real ######
				if 'R' in Tipo:
					if (random.random()<.8):
						return [ setVar[ random.randint( 0, len(setVar)-1 ) ] ]#Retorna una variable al azar
					else :
						return [ setVarCon[ random.randint( 0, len(setVarCon)-1 ) ] ]
				
				##### Binaria ####
				elif 'Log' in Tipo:
					return [ setVarConB[ random.randint( 0, len(setVarConB)-1 ) ] ]#Retorna una variable al azar
				##### Bloque  ####
				elif 'MuB' in Tipo:
					return ['None']
					
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
			return not X[0] 
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
			I = int(self.evaluar(val, X[2]) )
			J = int (self.evaluar(val, X[1]) )
			#print I
			#print J
			conStopFor = 0 
			if I>10 or I<10:
				I = 10
			if J>10 or J<10:
				J = 10
			self.forVal.append(0)
			if I<J:
				for i in xrange(I,J ):
					self.forVal[len(self.forVal)-1] =i
					self.evaluar(val, X[0])
					if conStopFor >= 10:
						return
					conStopFor+=1
			else :
				for i in xrange(I,J,-1 ):
					self.forVal[len(self.forVal)-1] =i
					self.evaluar(val, X[0])
					if conStopFor >= 10:
						return
					conStopFor+=1

		elif 'while' == op:
			conStop = 10
			#print "Entro al while"
			while self.evaluar(val, X[1] ) and conStop:
				self.evaluar(val, X[0])
				conStop-=1
		elif 'if' == op:
			#print "Entro al if"
			if self.evaluar(val, X[2]):
				self.evaluar(val,  X[1])
			else:
				self.evaluar(val, X[0])
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







	def evaluar (self, val,pos):
		pila = []
		#print"########################### "
		#print pos 
		#print "###########################"
		for i in xrange(0, len(pos)):
			#print "fdgfd"
			#print pos[i]

			if ( pos[i] in setVar   ):
				#print "sta es : "+ pos[i]
				pila.append(val[ setVar.index(pos[i]) ])

			elif str(type(pos[i])) == "<type 'list'>": 
				pila.append(pos[i])
			elif pos[i] in setVarCon:
				pila.append( valCon[setVarCon.index(pos[i])] )
			elif pos[i] in setVarConB:
				pila.append( valConB[setVarConB.index(pos[i])] )
			elif pos[i] in setFunSimple[0] :
				indfun = setFunSimple[0].index(pos[i])
				param = []
				for j in xrange(0,setFunSimple[1][indfun]):
					param.insert(0, pila.pop() ) 
				#print param
				res = self.operador(val,pos[i],param)
				pila.append(res)
			elif pos[i][0:3] == 'for':
				ind = int(pos[i][3:][0])
				if ind <= len(self.forVal):
					pila.append( self.forVal[ind-1] )
				else:
					pila.append(0)
		return pila.pop()

	def evaluarGen(self, val):
		#print "---------------------"
		#print self.gen
		#print "---------------------"
		self.resultado = []
		self.evaluar(val,self.gen)
		return self.resultado
		#print  inst

	###################### Evaluacion #######################################
	def operadorIm (self,op, X):
		global setFun
		global setVar
		########### logicos ############
		if 'and' == op:
			return "("+str(X[0])+" and "+str(X[1])+")"
		elif 'or' == op:
			return "("+str(X[0])+ " or " +str(X[1])+")"  
		elif 'not' == op:
			return "(not "+str(X[0])+")" 
	   	######### Aritmeticos ###########
		elif '+' == op:
			return "("+str(X[0])+ " + " +str(X[1])+")"
		elif '-' == op:
			return "("+str(X[0])+ " - " +str(X[1])+")"
		elif '/' == op:
			return "("+str(X[0])+ " / " +str(X[1])+")"
		elif '*' == op:
			return "("+str(X[0])+ " * " +str(X[1])+")"  
		############ condicionales ############
		elif '<' == op:
			return "("+str(X[0])+ " < " +str(X[1])+")"  
		elif '>' == op:
			return "("+str(X[0])+ " > " +str(X[1])+")"  
		elif '==' == op:
			return "("+str(X[0])+ " == " +str(X[1])+")"  
		elif '!=' == op:
			return "("+str(X[0])+ " != " +str(X[1])+")"
		elif '>=' == op:
			return "("+str(X[0])+ " >= " +str(X[1])+")"
		elif '<=' == op:
			return "("+str(X[0])+ " <= " +str(X[1])+")"  
		########## Iterativo ############

		elif 'for' == op:
			#print "Entro al for"
			#I = int( )
			#J = int (self.evaluar(val, X[1]) )
			#print I
			#print J
			#conStopFor = 0 
			#if I>10 or I<10:
			#	I = 10
			#if J>10 or J<10:
			#	J = 10
			#self.forVal.append(0)
			print "for ( "+ self.imprimir(X[2]) +" , "+ self.imprimir(X[2]) + ", +1 ){"
			self.imprimir(X[0])
			print "}"

		elif 'while' == op:
			
			print "while ( "+self.imprimir(X[1])+" ){"
			self.imprimir(X[0])
			print "}"

		elif 'if' == op:
			
			#print "Entro al if"
			print "if ( "+self.imprimir(X[2])+" ) {"
			self.imprimir( X[1])
			print "}"
			print "else { "
			self.imprimir(X[0])
			print "}"

		elif 'print' ==  op:
			print "print "+ str(X[0])

		######### Multiblock ######
		elif 'block2' == op :
			print '{'
			self.imprimir( X[0])
			self.imprimir( X[1])
			print '}'
		elif 'block3' == op :
			print '{'
			self.imprimir( X[0])
			self.imprimir( X[1])
			self.imprimir( X[2])
			print '}'
		elif 'block4' == op :
			print '{'
			self.imprimir( X[0])
			self.imprimir( X[1])
			self.imprimir( X[2])
			self.imprimir( X[3])
			print '}'
		elif 'block5' == op :
			print '{'
			self.imprimir( X[0])
			self.imprimir( X[1])
			self.imprimir( X[2])
			self.imprimir( X[3])
			self.imprimir( X[4])
			print '}'

	def imprimir (self,pos):
		pila = []
		#print"########################### "
		#print pos 
		#print "###########################"
		for i in xrange(0, len(pos)):
			#print "fdgfd"
			#print pos[i]

			if ( pos[i] in setVar   ):
				pila.append(pos[i])
			elif str(type(pos[i])) == "<type 'list'>": 
				pila.append(pos[i])
			elif pos[i] in setVarCon:
				pila.append( str(valCon[setVarCon.index(pos[i])]) )
			elif pos[i] in setVarConB:
				pila.append( str(valConB[setVarConB.index(pos[i])]) )
			elif pos[i] in setFunSimple[0] :
				indfun = setFunSimple[0].index(pos[i])
				param = []
				for j in xrange(0,setFunSimple[1][indfun]):
					param.insert(0, pila.pop() ) 
				#print param
				res = self.operadorIm(pos[i],param)
				pila.append(res)
			elif pos[i][0:3] == 'for':
				ind = int(pos[i][3:][0])
				if ind <= len(self.forVal):
					pila.append( pos[i] )
				else:
					pila.append('0')
		return pila.pop()

"""
prueba = Individuo(5)
print prueba.gen
prueba.imprimir(prueba.gen)
res = prueba.evaluarGen([5,4,4,8,10,9,3,7])
print "el resultado es "
print res
"""