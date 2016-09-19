import numpy as np
import Posfija

def aleatorio( n=2, prof=0 ):
	poblacion = []
	for i in xrange(0,n) :
		poblacion.append( Posfija.crear(prof) )
	return poblacion

"""
print aleatorio(2,3)
"""