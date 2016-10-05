import Individuo
import copy
import PoblacionInicial
import random

PM = 6
candidato = []
 




def Punto(Can):

	Can1 = copy.copy(Can[0].gen)
	Can2 = copy.copy(Can[1].gen)
	N[0] = random.randint(0,len(Can1)-1)
	N[1] = random.randint(0,len(Can2)-1)

	# print "con pivote " + str(ind)
	if random.random()*10 < PM:

		print N[0]
		print N[1]
		RCan1 = []
		RCan2 = []
		RCan1 = [N[0]+1:len(Can1)]
		sum = 1
		indC = N[0]
		while num != 0:
			num-=1
			if  Can1[indC] in Individuo.setFun :
				indNpara = Individuo.setFun[0].index(Can1[indC])
				num += Individuo.setFun[1][indNpara]
			indC-=1
		RCan1aux = [0:indC+1]

		RCan1aux2 = []
		sum = 1
		indC = N[1]
		while num != 0:
			num-=1
			RCan1aux2.insert(0,Can2[indC])
			if  Can2[indC] in Individuo.setFun :
				indNpara = Individuo.setFun[0].index(Can1[indC])
				num += Individuo.setFun[1][indNpara]
			indC-=1
		res = RCan1aux2+RCan1aux+RCan1

			


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