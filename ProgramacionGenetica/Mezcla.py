import Posfija
import Individuo
import copy
import PoblacionInicial
import random

PM = 6
candidato = []
N = [0,0]
varEst =[0,0]
 
def recuMez (r):
	global varEst

	if varEst[r]<len(candidato[r].gen):
		aux = candidato[r].gen[varEst[r]]
		indAc = varEst[r]
		#print aux
		#print varEst[r]
		#print N[r]
		if ( aux in Posfija.setVar or type(aux) == type(1.0) ):
			if indAc != N[r] :
				return [aux]
			else :
				#print "----------cruze------------"
				if r == 0 :
					return recuMez2(1)
				else: 
					return recuMez2(0)

		elif aux in Posfija.setFun :
			varEst[r] += 1
		 	a = recuMez(r)
		 	varEst[r] += 1
		 	b = recuMez(r)
		 	#print a
		 	#print b
		 	if indAc != N[r] :
				return [aux] + a + b 
			else :
				#print "----------cruze------------"
				if r == 0 :
					return recuMez2(1)
				else: 
					return recuMez2(0)  

def recuMez2 (r):
	global varEst

	if varEst[r]<len(candidato[r].gen):
		aux = candidato[r].gen[varEst[r]]
		
		if ( aux in Posfija.setVar or type(aux) == type(1.0) ):
			return [aux]
		elif aux in Posfija.setFun :
			indAc = varEst[r]
			varEst[r] += 1
		 	a = recuMez2(r)
		 	varEst[r] += 1
		 	b = recuMez2(r)
			return [aux]+a+b 

def Punto(Can):

	global varEst 
	global candidato
	global N

	preci1 = len(Can[0].gen)
	preci2 = len(Can[1].gen)

	candidato = copy.copy(Can)


	N[0] = random.randint(0,preci1-1)
	N[1] = random.randint(0,preci2-1)
	varEst[0] = 0
	varEst[1] = N[1]
	recuMez(0)
	print "segunda mezcla"
	varEst[0] = N[0]
	varEst[1] = 0
	recuMez(1)

	# print "con pivote " + str(ind)
	if random.random()*10 < PM:


		N[0] = random.randint(0,preci1-1)
		N[1] = random.randint(0,preci2-1)
		varEst[0] = 0
		varEst[1] = N[1]
		print N[1]
		rMez1 = recuMez(0)
		varEst[0] = N[0]
		varEst[1] = 0
		print N[0]
		rMez2 = recuMez(1)
		candidato[0].gen = rMez1
		candidato[1].gen = rMez2
		return [copy.copy(candidato[0]), copy.copy(candidato[1]) ] 
	else:
		return [ copy.copy(candidato[0]), copy.copy(candidato[1])  ]
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
"""	
Pob = PoblacionInicial.aleatorio(2,2)
for i in Pob:
	print i.gen 

a = Punto(Pob)
for i in a:
	print i.gen 
	print Posfija.evaluar(i.gen,[1])
"""