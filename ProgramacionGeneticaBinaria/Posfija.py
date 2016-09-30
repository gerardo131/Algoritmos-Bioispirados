import random

##################### inicializacion del modulo ####################

# METODO  ----- Metodo para crear exprecion posfija FULL, GROW o HALF-AND-HALF
# setFun ----- Conjunto de funciones 
# numVar ----- Numero de variables 
# conInter --- Intervalo de constante
# Pvar  ------ probabilidad de escojer variables    
# Pconstan --- probabilidad de escojer constantes 
# PFun ------- probabilidad de escojer funciones    

############ Funciones ##########

# crear ---------Crea la exprecion posfija   
# operadores ----Especifica el funcionamiento de cada una de las funciones (operador)
# evaluar -------Evalua la exprecion posfija 

####################################################################
varEst=0
valor =[]
posfija =[]

METODO = "FULL" 
setFun=['and','or','not']
setVar= [chr(i) for i in xrange(97,97+25)] + [chr(i) for i in xrange(97-32,97-7)]
numVar = 3

#------- Probabilidades de cada uno de los signos ------------
PVar = 8
PConstan = 1
#-------------------------------------------------------------


###################### CREAR #########################
def full (n):
	global numVar
	if (n==0):
		return [ setVar[ random.randint(0,numVar-1) ] ] #Retorna una variable al azar
	else:
		fun = setFun[ random.randint( 0 , len(setFun)-1 ) ]
		if (fun=='not'):
			return [fun]+full(n-1)
		else:
			return [fun]+full(n-1)+full (n-1)

def grow (n):
	if (n==0 or  (random.random()*10 < .3 )  ):
		return [ setVar[int(random.random()*len(setVar))] ] # retorna una variable al azar
	else:
		return [ setFun [0] ] + full (n-1)+ full (n-1)

def crear (n=0,nInd=-1):
	if METODO == "FULL" :
		
		if nInd == -1 :
			return full(n)
		else:
			ind=[]
			for i in xrange(0,nInd):
				ind.append(full(n))
			return ind

	elif METODO == "GROW":
		pass
	elif METODO == "HALF-AND-HALF" :
		pass


######################## EVALUACION ##########################
def operadores (op,x=0,y=0):
	global setFun
	global setVar
	
	if setFun[0] == op:
		return (x and y)
	elif setFun[1] == op:
		return (x or y)
	elif setFun[2] == op:
		if not x :
			return 1
		else :
			return 0


def evaluarRecu():
	global posfija
	global valor
	global setFun
	global setVar
	global varEst
	#print str(varEst) +"   " +str(len(posfija))

	if varEst<len(posfija): 
		if ( posfija[varEst] in setVar ):
			ind = setVar.index( posfija[varEst] )
			return valor[ind]
		elif ( posfija[varEst] in setFun ):
				if (posfija[varEst] == 'not'):
					indAc = varEst
					varEst = varEst+1
					a = evaluarRecu()
					return operadores(posfija[indAc], a)
				else :
					indAc = varEst
					varEst = varEst+1
				 	a = evaluarRecu()
				 	varEst = varEst+1
				 	b = evaluarRecu()
				 	return operadores(posfija[indAc], a, b)
	

def evaluar (pos,val):

	global posfija
	global valor
	global varEst
	varEst = 0 
	valor = val
	posfija = pos



	res =  evaluarRecu()
	return res


##############################################################
"""
#----------------codigo de inicializacion -------------
METODO == "FULL"
setFun=['+','-','/','*']
conInter = (.5,.5)
numVar = 2 

#------------------------------------------------------
#--------------- Prueba de evaluacion y creacion full ----- 

print "crear cadena con metodo FULL"
fr = crear(1,2)
print fr
print "evaluar cadena con metodo FULL"
fe = evaluar(['+','/',4.0,2.0,'*',3.0,5.0],[8,8,8,8,8] ) 
print str(fe) + "  " + str(fe == 64) 

#----------------------------------------------------------
"""
print "crear cadena con metodo FULL"
fr = crear(2,3)
print fr