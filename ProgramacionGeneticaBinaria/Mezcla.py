import Individuo

import copy
import PoblacionInicial
import random

PM = 6
candidato = []
 
def mezclaPunto(Can1,Can2,N):

	RCan1 = []
	RCan2 = []
	RCan1 = Can1[N[0]+1:len(Can1)]
	num = 1
	indC = N[0]
	while num != 0:
		num-=1
		if  Can1[indC] in Individuo.setFun[0] :
			indNpara = Individuo.setFun[0].index(Can1[indC])
			num += Individuo.setFun[1][indNpara]
		indC-=1
	RCan1aux = Can1[0:indC+1]

	RCan1aux2 = []
	num = 1
	indC = N[1]
	while num != 0:
		num-=1
		RCan1aux2.insert(0,Can2[indC])
		if  Can2[indC] in Individuo.setFun[0] :
			indNpara = Individuo.setFun[0].index(Can2[indC])
			num += Individuo.setFun[1][indNpara]
		indC-=1
	res = RCan1aux+RCan1aux2+RCan1
	return res 




def Punto(Can):

	Can1 = copy.copy(Can[0])
	Can2 = copy.copy(Can[1])
	N=[0,0]
	N[0] = random.randint(0,len(Can[0].gen)-1)
	N[1] = random.randint(0,len(Can[1].gen)-1)

	# print "con pivote " + str(ind)
	if random.random()*10 < PM:
		RCan1 = mezclaPunto(Can1.gen,Can2.gen,N)
		RCan2 = mezclaPunto(Can2.gen,Can1.gen,[N[1],N[0]])
		Can1.gen = RCan1
		Can2.gen = RCan2
	return [ Can1, Can2 ]
"""
pru1 = Individuo.Individuo(2)
pru2 = Individuo.Individuo(2)
print pru1.gen 
print pru2.gen
P= Punto ([pru1,pru2])
for i in P:
	print i.gen
"""
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