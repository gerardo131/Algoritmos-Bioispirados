import Individuo

################### funcion de adaptacion ############################3

def adaptacion(pob,valE,resE):
	Aerror = []
	for i in pob:
		Aerror.append( i.error(valE,resE) )
	for i in xrange( 0,len(pob) ):
		pob[i].calificacion = max(Aerror)+min(Aerror)- pob[i].error
