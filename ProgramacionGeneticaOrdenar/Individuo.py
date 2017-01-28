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
		self.Nfor = 0
		self.forVar = []
		self.regiFor = []
		self.gen = self.crearCadena(prof)
		self.calificacion = 0
		self.error = 0
		self.resultado = []
		self.NumWhile = 0



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
########### REGLAS DE CONSTRUCCION #########
# El for simpre tendra como primer parametro un arbol que represente la asignacion de una varible propia del for 
#
	def grow(self,prof,Tipo=['MB']):
		if (prof == 0):
			############## Si ya esmos en las hojas del arbol selecionamos un nodo terminal de forma aleatoria con respecto al tipo de de dato aceptado ####
			opcionesRe = []
			for i in Tipo:
				opcionesRe = reglas.TerAndTy[i]+opcionesRe
				
			return [ random.choice(opcionesRe) ]
		else:
			######## Si queremos poner una funcion en el árbol ############################
			opcionesRe = []
			for i in Tipo:
				opcionesRe = reglas.FunAndTy[i]+opcionesRe
			if (random.random()<.9 and len(opcionesRe)!= 0 or (len(Tipo)==1 and 'MB' in Tipo) ) :    
				fun = random.choice(opcionesRe) # Selecciona aleatoriamente la funcion con un espesifico tipo de dato de retorno
				exp = [fun]                     # Contruye el arreglo para contruir la exprecion de la rama actual         
				regPar = reglas.FunPar[fun]     # Guardamos la regla que se usara para escojer los tipos de parametros aceptados 
				
				#### El conjunto de Multi Bloque (MB) los contruimos encapsulando sus parametros en un araglo #############  
				if fun in reglas.FunAndTy['MB']:
					# for contiene una restriccion de contrucción debido a su variable local que contiene 
					if fun == 'for':
						self.Nfor += 1
						self.NF =self.Nfor
						exp =  [self.grow(prof-1,regPar['TypePar'][0])] + exp 
						self.forVar.append(  )
						exp =  [self.grow(prof-1,regPar['TypePar'][1])] + exp
						exp =  [self.grow(prof-1,regPar['TypePar'][2])] + exp
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
					opcionesRe = reglas.TerAndTy[i]+opcionesRe
				print prof 
				print opcionesRe
				return [ random.choice(opcionesRe) ]
					
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
			I = int(self.evaluar( X[2]) )
			J = int (self.evaluar( X[1]) )
			conStopFor = 0 
			if I>10 or I<10:
				I = 10
			if J>10 or J<10:
				J = 10
			self.forVal.append(0)
			if I<J:
				for i in xrange(I,J ):
					self.forVal[len(self.forVal)-1] =i
					self.evaluar( X[0])
					if conStopFor >= 10:
						return
					conStopFor+=1
			else :
				for i in xrange(I,J,-1 ):
					self.forVal[len(self.forVal)-1] =i
					self.evaluar( X[0])
					if conStopFor >= 10:
						return
					conStopFor+=1

		elif 'while' == op:
			conStop = 10
			while self.evaluar( X[1] ) and conStop:
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
			self.valIntPut[setVarLoc.index(X[1][0])] = self.evaluar(X[0])


	def evaluar (self,pos):
		pila = []
		#print"########################### "
		#print pos 
		#print "###########################"
		for i in xrange(0, len(pos)):
			print pos[i]
			if ( pos[i] in reglas.TerAndTy["MeR"]   ):
				print self.valVar[pos[i]]
				pila.append(self.valVar[pos[i]])
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
				res = self.operador(pos[i],param)
				pila.append(res)
			elif pos[i][0:3] == 'for':
				ind = int(pos[i][3:][0])
				if ind <= len(self.forVal):
					pila.append( self.forVal[ind-1] )
				else:
					pila.append(0)
		return pila.pop()

	def evaluarGen(self,val):
		#print "---------------------"
		#print self.gen
		#print "---------------------"
		for i in xrange(0, len(reglas.InputVar)) :
			self.valVar[reglas.InputVar[i]["Name"]] = val[i] 
		self.resultado = []
		self.evaluar(self.gen)
		return self.resultado
		#print  inst

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
			print "for ( "+ self.imprimir(X[2]) +" ; "+ self.imprimir(X[2]) + "; +1 ){"
			self.imprimir(X[0])
			print "}"

		elif 'while' == op:
			self.NumWhile+=1
			NumW = self.NumWhile
			print "int VarWhile"+str(NumW)+" = 0;"
			print "if (VarWhile"+str(NumW)+" < 20){"
			print "while ( "+self.imprimir(X[1])+" ){"
			self.imprimir(X[0])
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
			self.imprimir( X[1])
			print '}'
		elif 'Block3' == op :
			print '{'
			self.imprimir( X[0])
			self.imprimir( X[1])
			self.imprimir( X[2])
			print '}'
		elif 'Block4' == op :
			print '{'
			self.imprimir( X[0])
			self.imprimir( X[1])
			self.imprimir( X[2])
			self.imprimir( X[3])
			print '}'
		elif 'Block5' == op :
			print '{'
			self.imprimir( X[0])
			self.imprimir( X[1])
			self.imprimir( X[2])
			self.imprimir( X[3])
			self.imprimir( X[4])
			print '}'
		elif '=R' == op :
			print X[1][0]+" = " + self.imprimir(X[0])+";" 
		elif '$R' == op :
			return X[0]

	def imprimir (self,pos):
		pila = []
		#print"########################### "
		#print pos 
		#print "###########################"
		for i in xrange(0, len(pos)):
			if ( pos[i] in reglas.NameVar ):
				pila.append(pos[i])
			elif ( pos[i] in reglas.NameCons ):
				pila.append(str(reglas.ValCons[pos[i]]))
			elif str(type(pos[i])) == "<type 'list'>": 
				pila.append(pos[i])
			elif pos[i] in reglas.Funcion :
				param = []
				for j in xrange(0,reglas.FunPar[pos[i]]['NumPar']):
					param.insert(0, pila.pop() ) 
				#print param
				res = self.operadorIm(pos[i],param)
				pila.append(res)
		return pila.pop()
	def imprimirGen(self,val):
		#print "---------------------"
		#print self.gen
		#print "---------------------"
		print "int main(int argc, char const *argv[]){"
		for i in xrange(0, len(reglas.InputVar)) :
			print "float "+ reglas.InputVar[i]["Name"] +"="+ str(val[i])+";"
		for i in xrange(0, len(reglas.FreeVar)) :
			print "float "+ reglas.FreeVar[i]["Name"] +"="+ "0.0"+";" 

		self.imprimir(self.gen)
		print "}"

prueba = Individuo(5)
print prueba.gen
prueba.imprimirGen([5,4,4,8,10,9,3,7,7,2])
#res = prueba.evaluarGen()
#print "el resultado es "
#print res
