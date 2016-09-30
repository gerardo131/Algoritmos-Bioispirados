import Posfija 
import Individuo

def function():
	pass

################### funcion de adaptacion ############################3


def adaptacion(pob,valE,resE):
	Aerror = []
	for i in pob:
		Aerror.append( error(i.gen,valE,resE) )
	for i in xrange( 0,len(pob) ):
		pob[i].calificacion =max(Aerror)+min(Aerror)- Aerror[i]
		pob[i].error = Aerror[i]

def error(exp,valE,resE):
	val = 0 
	for i in xrange(0,len(valE)): 
		val += ( Posfija.evaluar(exp,valE[i]) - resE[i] )**2
	val /= len(valE) 
	print val
	return val

