import Individuo

import copy
import PoblacionInicial
import random
 
def mezclaPunto(Can1,Can2,N):

	Can1 = str(Can1).replace('[','').replace(']','').replace('\'','').split(', ')
	Can2 = str(Can2).replace('[','').replace(']','').replace('\'','').split(', ')
	RCan1 = []
	RCan1 = Can1[N[0]+1:len(Can1)]
	num = 1
	indC = N[0]
	
	while num != 0:
		num-=1
		if  Can1[indC] in Individuo.setFunSimple[0] :
			indNpara = Individuo.setFunSimple[0].index(Can1[indC])
			num += Individuo.setFunSimple[1][indNpara]
		indC-=1
	RCan1aux = Can1[0:indC+1]

	RCan1aux2 = []
	num = 1
	indC = N[1]
	while num != 0:
		num-=1
		RCan1aux2.insert(0,Can2[indC])
		if  Can2[indC] in Individuo.setFunSimple[0] :
			indNpara = Individuo.setFunSimple[0].index(Can2[indC])
			num += Individuo.setFunSimple[1][indNpara]
		indC-=1
	res = RCan1aux+RCan1aux2+RCan1
	return res 


def Punto(Can,PC = 100):

	Can1 = copy.copy(Can[0])
	Can2 = copy.copy(Can[1])
	N=[0,0]
	lenCan1 = str(Can[0].gen).replace('[','').replace(']','').replace('\'','').split(', ')
	lenCan2 = str(Can[1].gen).replace('[','').replace(']','').replace('\'','').split(', ')
	N[0] = random.randint(0,len(lenCan1)-1)
	N[1] = random.randint(0,len(lenCan2)-1)

	# print "con pivote " + str(ind)
	if random.random()*100 < PC:
		RCan1 = mezclaPunto(Can1.gen,Can2.gen,N)
		RCan2 = mezclaPunto(Can2.gen,Can1.gen,[N[1],N[0]])
		Can1.gen = RCan1
		Can2.gen = RCan2
	return [ Can1, Can2 ]

#def recorido(gen):
	#while :
	#	pass

###############    PRUEBA    ####################


pru1 = Individuo.Individuo(2)
pru2 = Individuo.Individuo(2)
print pru1.gen 
print pru2.gen

P= Punto ([pru1,pru2])
for i in P:
	print i.gen


#################################################