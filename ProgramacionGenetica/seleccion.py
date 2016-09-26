import Individuo
import random
import copy

#----------------------- seleccion -------------------------------
def ruleta(pob):
	sumCal = 0
	res = []
	for j in xrange(0,2):
		calAcom=0
		for k in xrange(0,len(pob)):
			sumCal += pob[k].calificacion
		r = random.random()
		rand = r*sumCal
		i=0
		while(i<len(pob) and calAcom<rand ):
			calAcom += pob[i].calificacion
			i+=1
		if i==len(pob) :
			res.append( copy.copy(pob[i-1]) )
		else :
			res.append(copy.copy(pob[i]) )
	"""
	print "generacion"
	print res
	print "----------"
	"""
	return res