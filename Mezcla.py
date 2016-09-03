import math
import random
import numpy as np

#-------------------------- Mezclar ------------------------------

def puntos(Can1, Can2):
	canMez1 =[]
	canMez2 =[]
	
	nvar=len(Can1)
	preci=len(Can1[0])
	
	ind=random.randint(0,(preci)*nvar-1)

	# print "con pivote " + str(ind)
	if random.randint(0,1) == 0 :

		for i in xrange(0,nvar):
			ind1=[]
			ind2=[]
			for j in xrange(0,preci):
				if(i*preci+j)<ind :
					ind1.append( Can1[i][j] )
	  				ind2.append( Can2[i][j] )
				else:
					ind1.append( Can2[i][j] )
					ind2.append( Can1[i][j] )
			canMez1.append(ind1)
			canMez2.append(ind2)
	else:
		canMez1 = Can1
		canMez2 = Can2
	"""

	print "Mezclar : " 
	print "candidato uno"
	for i in xrange(0,nvar):
		print str(dCodBin(Can1[i]) ) 
	print "candidato dos"
	for i in xrange(0,nvar):
		print str(dCodBin(Can2[i]) ) 
	print "----------------------------------"
	print "Resultado : " 
	print "candidato uno"
	for i in xrange(0,nvar):
		print str(dCodBin(canMez1[i]) ) 
	print "candidato dos"
	for i in xrange(0,nvar):
		print str(dCodBin(canMez2[i]) ) 
	print "----------------------------------"	
	"""
	return canMez1,canMez2