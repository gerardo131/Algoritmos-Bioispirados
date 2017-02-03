#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
from operator import xor
import reglas

##################### inicializacion del modulo ####################

# METODO  ----- Metodo para crear exprecion posfija FULL, GROW o HALF-AND-HALF
# setFun ----- Conjunto de funciones 
# numVar ----- Numero de variables 
# conInter --- Intervalo de constante
# Pvar  ------ probabilidad de escojer variables    
# Pconstan --- probabilidad de escojer constantes 
# PFun ------- probabilidad de escojer funciones    

metCrear = "GROW"
#------- Probabilidades de cada uno de los signos ------------
PVar = 8
PConstan = 1
#-------------------------------------------------------------

class Individuo:
	

	def __init__(self, prof):
		self.NameVarVal = {}
		#Son arreglos que contienen los tipos de datos y el nombre de la funciones 
		self.TerAndTy = reglas.TerAndTy
		self.FunAndTy = reglas.FunAndTy 
		self.DinVartry = reglas.DinVartry 

		# Son arreglos que contiene todos los nombres de las funciones
		self.Funcion  =	reglas.Funcion[:]    
		self.Terminal =	reglas.Terminal[:]   
		self.DinamicVar =	reglas.DinamicVar[:]   
		self.NameInputVar =	reglas.NameInputVar[:]   
		self.NameFreevar  =	reglas.NameFreevar[:]    
		self.NameVar      =	reglas.NameVar[:]      
		self.NameCons     =	reglas.NameCons[:]    
		self.InputVar = reglas.InputVar[:]  
		self.FreeVar = reglas.FreeVar[:]
		self.DinVar = reglas.DinVar[:]
		#Son arreglos con el nombre de las constantes y el valor 
		self.ValCons  = reglas.ValCons 


		#Contiene  el nombre y el numero de parametros y el tipo de cada parametro
		self.FunPar =  reglas.FunPar


		self.Nfor = 0
		self.forVar = []
		self.gen = self.crearCadena(prof)
		self.calificacion = 0
		self.error = 0
		self.resultado = []
		self.NumWhile = 0
		self.NumFor = 0



	################### funcion de adaptacion ############################
	def EMC(self,valE,resE):
		val = 0.0 
		for i in xrange(0,len(valE)): 
			parVal = 0.0
			res = self.evaluarGen(valE[i])
			#print res
			for j in xrange(0,len(resE[i])) :
				if res[j] != resE[i][j]:
					parVal += 1.0
			val += float(parVal)/float(len(resE[i]))

		val = (val)/float(len(valE)) 
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
########### self DE CONSTRUCCION #########
# El for simpre tendra como primer parametro un arbol que represente la asignacion de una varible propia del for 
#
	def grow(self,prof,Tipo=['MB']):
		if (prof == 0):
			############## Si ya esmos en las hojas del arbol selecionamos un nodo terminal de forma aleatoria con respecto al tipo de de dato aceptado ####
			opcionesRe = []
			for i in Tipo:
				opcionesRe = self.TerAndTy[i]+opcionesRe
			genuinas = opcionesRe[:]
			if "R" in Tipo:
				opcionesRe = self.forVar+opcionesRe+self.NameFreevar+self.NameInputVar
				terminaSel = random.choice(opcionesRe)
				if terminaSel in self.NameInputVar:
					ind = [terminaSel[4:]]
					return [  random.choice(self.forVar+genuinas) ,"$AR","$R"]
				if terminaSel in self.NameFreevar:
					return [  terminaSel  ,"$R"]
			
			if "MeR" in Tipo:
				opcionesRe = opcionesRe+self.NameFreevar+self.NameInputVar
				terminaSel = random.choice(opcionesRe)
				if terminaSel in self.NameInputVar:
					ind = [terminaSel[4:]]
					return [  random.choice(self.forVar+reglas.ConsAndTy["R"]) ,"$AR"]
				
			terminaSel = random.choice(genuinas)
			return [terminaSel  ]
		else:
			######## Si queremos poner una funcion en el árbol ############################
			opcionesRe = []
			for i in Tipo:
				opcionesRe = self.FunAndTy[i]+opcionesRe
			if (random.random()<.9 and len(opcionesRe)!= 0 or (len(Tipo)==1 and 'MB' in Tipo) ) :  
				if prof == 1 and "MB" in Tipo:
					opcionesRe = ["=R"] 
				fun = random.choice(opcionesRe) # Selecciona aleatoriamente la funcion con un espesifico tipo de dato de retorno
				exp = [fun]                     # Contruye el arreglo para contruir la exprecion de la rama actual         
				regPar = self.FunPar[fun]     # Guardamos la regla que se usara para escojer los tipos de parametros aceptados 
				
				#### El conjunto de Multi Bloque (MB) los contruimos encapsulando sus parametros en un araglo #############  
				if fun in self.FunAndTy['MB']:
					# for contiene una restriccion de contrucción debido a su variable local que contiene 
					if fun == 'for':
						self.Nfor += 1
						self.NF =self.Nfor
						exp =  [self.grow(prof-1,["R"])+["set-"+self.DinamicVar[self.Nfor]]] + exp 
						exp =  [self.grow(prof-1,regPar['TypePar'][1])] + exp
						self.forVar.append(self.DinamicVar[self.Nfor])
						exp =  [ self.grow(prof-1,regPar['TypePar'][2]) ] + exp
						self.forVar.pop()
						self.Nfor =0
						exp = exp

					else:
						for i in xrange (0,regPar['NumPar']):
							exp =  [self.grow(prof-1,regPar['TypePar'][i])] + exp
						exp = exp

				else : 
				###### El  cunjunto de funciones lo contruimos concatenando cada una de sus expreciones futuras ##########
					for i in xrange (0,regPar['NumPar']):
						a = self.grow(prof-1,regPar['TypePar'][i])
						exp =  a + exp
				
				return exp
			else :
				############# Si queremos poner un terminal en lugar de una función y truncar el árbol 
				opcionesRe = []
				for i in Tipo:
					opcionesRe = self.TerAndTy[i]+opcionesRe
				genuinas = opcionesRe[:]
				if "R" in Tipo:
					opcionesRe = self.forVar+opcionesRe+self.NameFreevar+self.NameInputVar
					terminaSel = random.choice(opcionesRe)
					if terminaSel in self.NameInputVar:
						ind = [terminaSel[4:]]
						return [  random.choice(self.forVar+genuinas) ,"$AR","$R"]
					if terminaSel in self.NameFreevar:
						return [  terminaSel  ,"$R"]
					
				terminaSel = random.choice(genuinas)
				return [terminaSel  ]
					
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
		########### logicos ############
		if 'and' == op:
			return ( X[0]  and  X[1]) 

		elif 'or' == op:
			return ( X[0] or X[1] ) 
		elif 'not' == op:
			return not X[0] 
	   	######### Aritmeticos ###########
		elif '+' == op:
			#return X[0]+X[1]
			x=X[0]
			y=X[1]
			x_aux = 0.0
			y_aux = 0.0
			M = 2147483630.0
			if (x>=0 and y>=0):
				x_aux = M - x
				if ( x_aux - y < 0  ):
					return M
				else:
					return x+y

			elif(x<=0 and y<=0):
				x_aux = M + x
				if ( x_aux + y > 0 ):
					return M
				else :
					return x+y
				
			else:
				return x + y 
			
		elif '-' == op:
			x=X[0]
			y=X[1]
			x_aux = 0.0
			y_aux = 0.0

			M = 2147483630.0
			if (x>0 and y<0):
				x_aux = M - x
				if ( x_aux + y < 0 ):
					return M
				else:
					return x+y

			elif(x<0 and y>0):
				x_aux = M + x
				if ( x_aux - y > 0 ):
					return M
				else: 
					return x+y
			else:
				return x + y 
			
		elif '/' == op:
			if X[1] == 0.0  :
				return 0.0
			else :
				return X[0]/X[1]
		elif '*' == op:
			x=X[0]
			y=X[1]
			x_aux = 0.0;
			y_aux = 0.0;
			M = 2147483630.0;
			x_aux = x/M;
			if (x_aux*y<=1 and x_aux*y>=-1):
				return  x*y;
			return 2147483630.0; 
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
			#print "entro a for"
			I=0
			try:
				I , forVari = self.evaluar( X[2]) 
				J = int (self.evaluar( X[1]) )
				conStopFor = 0 
				for i in xrange(I,J ):
					#print conStopFor
					self.NameVarVal[forVari] =i
					self.evaluar( X[0])
					if conStopFor >= 10:
						return
					conStopFor+=1
			except Exception, e:
				print X[2]
				print X[1]
				print e
				raise


		elif 'while' == op:
			#print "entro a while"
			conStop = 10
			while self.evaluar( X[1] ) and conStop:
				#print conStop
				self.evaluar( X[0])
				conStop-=1
		elif 'if' == op:
			if self.evaluar( X[2]):
				self.evaluar(  X[1])
			else:
				self.evaluar( X[0])
		elif 'print' ==  op:
			self.resultado.append(X[0])

		######### Multiblock ######
		elif 'Block2' == op :
			self.evaluar(X[0])
			self.evaluar(X[1])
		elif 'Block3' == op :
			self.evaluar(X[0])
			self.evaluar(X[1])
			self.evaluar(X[2])
		elif 'Block4' == op :
			self.evaluar(X[0])
			self.evaluar(X[1])
			self.evaluar(X[2])
			self.evaluar(X[3])
		elif 'Block5' == op :
			self.evaluar(X[0])
			self.evaluar(X[1])
			self.evaluar(X[2])
			self.evaluar(X[3])
			self.evaluar(X[4])
		elif '=R' == op:
			self.NameVarVal[self.evaluar(X[1])] = self.evaluar(X[0]) 
		elif op.find("set-")>=0:
			#self.NameVarVal[op[4:]] = X[0]
			return int(X[0]),op[4:]
		elif '$AR' == op :
			print X[0]
			ind = int(X[0])%reglas.numInPutVar
			return "IPV_"+str(int(ind))
		elif '$R' == op :
			return self.NameVarVal[X[0]]
	def evaluar (self,pos):
		pila = []
		#print"########################### "
		#print pos 
		#print "###########################"
		for i in xrange(0, len(pos)):
			
			if ( pos[i] in self.NameInputVar+self.NameFreevar ):
				pila.append(pos[i])
			if ( pos[i] in self.DinamicVar ):
				pila.append(self.NameVarVal[pos[i]])
			elif str(type(pos[i])) == "<type 'list'>": 
				pila.append(pos[i])
			elif pos[i] in self.NameCons:
				pila.append( self.ValCons[pos[i]] )
			#elif pos[i] in setVarConB:
			#	pila.append( valConB[setVarConB.index(pos[i])] )
			elif pos[i] in self.Funcion :
				param = []
				for j in xrange(0,self.FunPar[pos[i]]['NumPar']):
					param.insert(0, pila.pop() ) 
				
				res = self.operador(pos[i],param)
				pila.append(res)
			elif pos[i].find("set-")>-1:
				param = []
				for j in xrange(0,self.FunPar[pos[i][0:4]]['NumPar']):
					param.insert(0, pila.pop() ) 
				
				res = self.operador(pos[i],param)
				pila.append(res)
		return pila.pop()

	def evaluarGen(self,val):
		#print "---------------------"
		#print self.gen
		#print "---------------------"

		for i in self.NameVar:
			self.NameVarVal[i]= 0.0
		for i in xrange(0, len(self.InputVar)) :
			self.NameVarVal[self.InputVar[i]["Name"]] = val[i] 
		self.resultado = []
		self.evaluar(self.gen)
		for i in xrange(0, len(self.InputVar)) :
			self.resultado.append( self.NameVarVal[self.InputVar[i]["Name"]] ) 
		return self.resultado
		#print  inst
	"""def evaluarGen(self,val):
		for i in xrange(0, len(self.InputVar)) :
			self.valVar[self.InputVar[i]["Name"]] = val[i] 	
	"""		
	###################### Evaluacion #######################################
	def operadorIm (self,op, X):
		########### logicos ############
		if 'and' == op:
			return "("+str(X[0])+" and "+str(X[1])+")"
		elif 'or' == op:
			return "("+str(X[0])+ " or " +str(X[1])+")"  
		elif 'not' == op:
			return "(not "+str(X[0])+")" 
	   	######### Aritmeticos ###########
		elif '+' == op:
			return "sum("+str(X[0])+ " , " +str(X[1])+")"
		elif '-' == op:
			return "res("+str(X[0])+ " , " +str(X[1])+")"
		elif '/' == op:
			return "div("+str(X[0])+ " , " +str(X[1])+")"
		elif '*' == op:
			return "mul("+str(X[0])+ " , " +str(X[1])+")"  
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
			self.NumFor+=1
			NumF = self.NumFor
			print "int VarFor"+str(NumF)+" = 0;"
			
			#print X[2]
			#print X[2][len(X[2])-1][4:]
			print "for ( "+ self.imprimir(X[2]) +" ; "+ X[2][len(X[2])-1][4:]+"<"+self.imprimir(X[1]) + ";"+X[2][len(X[2])-1][4:]+"++ ){"
			self.imprimir(X[0])
			print "if (VarFor"+str(NumF)+" > 20){"
			print "break;" 
			print "}"
			print "VarFor"+str(NumF)+"+=1;"
			print "}"
			
			
			self.NumFor = 0

		elif 'while' == op:
			self.NumWhile+=1
			NumW = self.NumWhile
			print "int VarWhile"+str(NumW)+" = 0;"
			print "while ( "+self.imprimir(X[1])+" ){"
			self.imprimir(X[0])
			print "if (VarWhile"+str(NumW)+" > 20){"
			print "break;" 
			print "}"
			print "VarWhile"+str(NumW)+"+=1;"
			print "}"
			self.NumWhile = 0

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
		elif 'Block2' == op :
			print '{'
			self.imprimir( X[0])
			print '}'
			print '{'
			self.imprimir( X[1])
			print '}'

		elif 'Block3' == op :
			print '{'
			self.imprimir( X[0])
			print '}'			
			print '{'
			self.imprimir( X[1])
			print '}'
			print '{'
			self.imprimir( X[2])
			print '}'

		elif 'Block4' == op :
			print '{'
			self.imprimir( X[0])
			print '}'
			print '{'
			self.imprimir( X[1])
			print '}'
			print '{'			
			self.imprimir( X[2])
			print '}'
			print '{'			
			self.imprimir( X[3])
			print '}'

		elif 'Block5' == op :
			print '{'
			self.imprimir( X[0])
			print '}'
			print '{'
			self.imprimir( X[1])
			print '}'
			print '{'
			self.imprimir( X[2])
			print '}'
			print '{'
			self.imprimir( X[3])
			print '}'
			print '{'
			self.imprimir( X[4])
			print '}'
			
		elif '=R' == op :
			print self.imprimir(X[1])+" = " + self.imprimir(X[0])+";" 
		elif op.find("set-")>-1:
			return op[4:] +" = " + X[0]
		elif '$AR' == op :
			#ind = int(X[0])%reglas.numInPutVar
			return "IPV[int("+X[0]+" % "+str(reglas.numInPutVar)+")]"
		elif '$R' == op :
			return X[0]

	def imprimir (self,pos):
		pila = []
		#print"########################### "
		#print pos 
		#print "###########################"
		for i in xrange(0, len(pos)):
			if ( pos[i] in self.NameVar ):
				pila.append(pos[i])
			elif ( pos[i] in self.NameCons ):
				pila.append(str(self.ValCons[pos[i]]))
			elif str(type(pos[i])) == "<type 'list'>": 
				pila.append(pos[i])
			elif pos[i] in self.Funcion :
				param = []
				for j in xrange(0,self.FunPar[pos[i]]['NumPar']):
					param.insert(0, pila.pop() ) 
				
				res = self.operadorIm(pos[i],param)
				pila.append(res)
			elif pos[i].find("set-")>-1:
				param = []
				for j in xrange(0,self.FunPar[pos[i][0:4]]['NumPar']):
					param.insert(0, pila.pop() ) 
				
				res = self.operadorIm(pos[i],param)
				pila.append(res)

		return pila.pop()

	def imprimirGen(self,val):
		#print "---------------------"
		#print self.gen
		#print "---------------------"
		print "#include \"DefOp.h\" "
		print "#include <iostream>"
		print "using namespace std;" 
		for i in self.ValCons :
			print "//"+ i +"="+ str(self.ValCons[i])+";"
		print "int main(int argc, char const *argv[]){"
		for i in xrange(0, len(self.InputVar)) :
			print "float IPV[] ="+ str(val).replace('[','{').replace(']','}')+";"
		for i in xrange(0, len(self.DinVar)) :
			print "float "+ self.DinVar[i]["Name"] +"="+ "1"+";"
		for i in xrange(0, len(self.FreeVar)) :
			print "float "+ self.FreeVar[i]["Name"] +"="+ "0.0"+";" 

		self.imprimir(self.gen)
		for i in xrange(0, len(self.InputVar)) :
			print "cout<<"+ self.InputVar[i]["Name"]+"<<endl;"
		print "return 0;"
		print "}"

prueba = Individuo(3)
print prueba.gen
#prueba.imprimirGen([5,4,4,8,10,9,3,7,7,2])
res = prueba.evaluarGen([5,4,4,8,10,9,3,7,7,2])
print "el resultado es "
print res
