import Individuo

################### funcion de adaptacion ############################3

def adaptacion(pob,valE,resE):
	Aerror = []
	for i in pob:
		i.EMC(valE,resE) 
	for i in xrange( 0,len(pob) ):
		pob[i].calificacion = 1000000.0- pob[i].error
