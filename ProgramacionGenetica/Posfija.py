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


METODO = "FULL" 
setFun=['+','-','/','*']
setVar= [chr(i) for i in xrange(97,97+25)] + [chr(i) for i in xrange(97-32,97-7)]
posfija =[]
numVar = 2
valor =[]
conInter = [-.5,.5]

#------- Probabilidades de cada uno de los signos ------------
PVar = 8
PConstan = 1
#-------------------------------------------------------------

###################### CREAR #########################
def full (n):
	global numVar
	if (n==0):

		if (random.random()*10 < PVar ):
			return [ setVar[ int(random.random()*numVar) ] ] # retorna una variable al azar
		else:
			return [float(random.random()*(conInter[1]-conInter[0])+conInter[0])]
	else:
		return [ setFun[ int(random.random()*len(setFun)) ] ] + full (n-1)+ full (n-1)

def grow (n):
	if (n==0 or  (random.random()*10 < .3 )  ):
		return [ setVar[int(random.random()*len(setVar))] ] # retorna una variable al azar
	else:
		return [ setFun [0] ] + full (n-1)+ full (n-1)

def crear (n=0):
	if METODO == "FULL" :
		return full(n)
	elif METODO == "GROW":
		pass
	elif METODO == "HALF-AND-HALF" :
		pass


######################## EVALUACION ##########################
def operadores (op,x,y):
	global setFun
	global setVar
	
	if setFun[0] == op:
		return x+y
	elif setFun[1] == op:
		return x-y
	elif setFun[2] == op:
		if y == 0 :
			return 0
		else :
			return x/y
	elif setFun[3] == op:
		return x*y  
varEst=0
def evaluarRecu():
	global posfija
	global valor
	global setFun
	global setVar
	global varEst

	if varEst<len(posfija): 

		if ( posfija[varEst] in setVar ):
			ind = setVar.index( posfija[varEst] )
			return valor[ind]
		elif (type(posfija[varEst]) == type(1.0)):
			return posfija[varEst]
		elif ( posfija[varEst] in setFun ):
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
	vatEst = 0
	valor = val
	posfija = pos

	return evaluarRecu()

##############################################################

#----------------codigo de inicializacion -------------
METODO == "FULL"
setFun=['+','-','/','*']
conInter = (.5,.5)
numVar = 2 

#------------------------------------------------------
#--------------- Prueba de evaluacion y creacion full ----- 

print "crear cadena con metodo FULL"
fr = crear(1)
print fr
print "evaluar cadena con metodo FULL"
fe = evaluar(['+','/',10.0,25.0,'*',4.0,5.0],[8,8,8,8,8] ) 
print str(fe) + "  " + str(fe == 64) 

#----------------------------------------------------------