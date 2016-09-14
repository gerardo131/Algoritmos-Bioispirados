import random

METODO = "FULL" 
setFun=['+','-','/','*']
setVar=[]
posfija =[]
numVar = 2
valor =[]
conInter = [-.5,.5]
PVar = 9
PConstan = 1

def setNumVar (num):
	global setVar 
	global numVar
	numVar = num
	setVar = [chr(i) for i in xrange(97,97+numVar)]

###################### CREAR #########################
def full (n):
	if (n==0):
		if (random.random()*10 < PVar ):
			return [ setVar[ int(random.random()*len(setVar)) ] ] # retorna una variable al azar
		else:
			return [float(random.random()*(conInter[1]-conInter[0])+conInter[0])]
	else:
		return [ setFun [0] ] + full (n-1)+ full (n-1)

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
		return x/y
	elif setFun[3] == op:
		return x*y  

def evaluarRecu(n):
	global posfija
	global valor
	global setFun
	global setVar

	if n<len(posfija): 

		if ( posfija[n] in setVar ):
			ind = setVar.index( posfija[n] )
			return valor[ind]
		elif (type(posfija[n]) == type(1.0)):
			return posfija[n]
		elif ( posfija[n] in setFun ):
			 a = evaluarRecu(n+1)
			 b = evaluarRecu(n+2)
			 return operadores(posfija[n], a, b)

def evaluar (pos,val):

	global posfija
	global valor
	valor = val
	posfija = pos

	return evaluarRecu(0)
##############################################################

#----------------codigo de inicializacion -------------
METODO == "FULL"
setFun=['+','-','/','*']
conInter = (.5,.5)
setNumVar (5)

#------------------------------------------------------


#--------------- Prueba de evaluacion y creacion full ----- 

print "crear cadena con metodo FULL"
fr = full(3)
print fr

print "evaluar cadena con metodo FULL"
fe = evaluar(fr,[8,8,8,8,8] ) 
print str(fe) + "  " + str(fe == 64) 

#----------------------------------------------------------

