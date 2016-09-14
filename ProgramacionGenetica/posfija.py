
arbol=[]
setFun=['+','-','/','*']
setVar=['a']

posfija =[]
valor = []

def full (n):
	if (n==0):
		return [ setVar[0] ]
	else:
		return [ setFun [0] ] + full (n-1)+ full (n-1)
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

		elif ( posfija[n] in setFun ):
			 a = evaluarRecu(n+1)
			 b = evaluarRecu(n+1)
			 return operadores(posfija[n], a, b)

def evaluar (pos,val):

	global posfija
	global valor
	valor = val
	posfija = pos

	return evaluarRecu(0)


r = full(3)
print evaluar(r,[8] ) 

