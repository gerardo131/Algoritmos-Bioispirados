import numpy as np
from Individuo import Individuo  

def aleatorio( n=2, prof=0 ):
	poblacion = []
	for i in xrange(0,n) :
		poblacion.append( Individuo(prof) )
	return poblacion

"""
print aleatorio(2,2)[0].gen
"""