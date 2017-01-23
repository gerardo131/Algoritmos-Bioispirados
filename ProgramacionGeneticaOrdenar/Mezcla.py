import Individuo
import copy
import PoblacionInicial
import random
 
def mezclaPunto(Can1,Can2,N):
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
	#print len(lenCan1)
	#print len(lenCan2)
	N[0] = random.randint(0,len(lenCan1)-1)
	N[1] = random.randint(0,len(lenCan2)-1)

	# print "con pivote " + str(ind)
	if random.random()*100 < PC:
		r,m,ite1 = contar(Can1.gen,N[0])
		print "###############"
		print r[m]
		print "###############"
		p,q,ite2 = contar(Can2.gen,N[1])
		print "###############"
		print p[q]
		print "###############"
		RCan1 = mezclaPunto(r,p,[m,q])
		RCan2 = mezclaPunto(p,r,[q,m])
	#	print RCan1
	#	print RCan2
		Can1.gen = recu (Can1.gen,ite1,0,RCan1)
		Can2.gen = recu (Can2.gen,ite2,0,RCan2)
	#	print Can1.gen
	#	print Can2.gen
	return [ Can1, Can2 ]
def recu (genM,iter,n,RCan):
	gen=genM[:]
	if n >= len(iter)-1  :
		return RCan
	else :
		try:
			gen[iter[n]]=recu(gen[iter[n]],iter,n+1,RCan)
		except Exception, e:
			
			print e
			print "iter :" +str(iter[n])
			print "gen : " + str(gen)
			exit()
		
		return gen

def contar(genM,N):
	#print " 00000 + " + str(N)
	gen=genM[:]
	a= str(gen).replace(' ','').replace('\'','').replace('[','[,').replace(']',',]').split(',')
	print a
	iter = [-1]
	i=1
	j=0
	while  j <= N:
		if  a[i] == '[':
		 	iter[len(iter)-1] += 1	
	 		iter.append(-1)
		elif a[i] == ']':
			iter.pop()
		else:
	 		j+=1
	 		iter[len(iter)-1] += 1
		i+=1
	print N
	print len(iter)
	print str(iter)

	#return  iter
	res = gen[:]
	for id in xrange(0,len(iter)-1):
		res = res[iter[id]][:]
	#print "Lo bueno"
	print res
	return res, iter[len(iter)-1],iter 
     	
   
     
	#	pass

###############    PRUEBA    ####################

pru1 = Individuo.Individuo(2)
pru2 = Individuo.Individuo(2)
print pru1.gen 
#contar ( pru1.gen, 5)
print pru2.gen

#print len(lenCan1)
#print len(lenCan2)

P= Punto ([pru1,pru2])
for i in P:
	print i.gen

#################################################

