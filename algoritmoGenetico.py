import math
from operator import xor
import random
import matplotlib.pyplot as plt

#---------------- Codificacion ---------------------------------

def codBin(num, preci):
	binNum=""
	Bin=""
	if num <0:
		Bin+="1"
		binNum=bin(num)[3:]
	else:
		Bin+="0"
		binNum=bin(num)[2:]
	for i in xrange(0,preci-len(binNum)):
		Bin+="0"
	Bin += binNum
	return list(Bin)
	
def dCodBin(Bin):
	
	if Bin[0]=="1":
		return -int(''.join(Bin[1:]),2)
	else:
		return int(''.join(Bin[1:]),2)  
#--------------------- Poblacion inicial ------------------------
def PoInAl(nind, nvar, preci):
	pob=[]
	for i in xrange(0,nind):
		ind =[]
		for j in xrange(0,nvar):
			fen=codBin(  random.randint (-6,6),preci)
			ind.append(fen)
		pob.append(ind)
	return pob
#------------------ funcion objetivo ----------------------------
def fobj(x):
	res=0
	for i in xrange(0,len(x)):
		res+=dCodBin(x[i])**2
	
	return res
#--------------------- Calificacion ----------------------------- 

def cal(pob): 
	val=[]
	aco=0
	for i in xrange(0,len(pob)):
		aco+=fobj(pob[i])
	for i in xrange(0,len(pob) ):
		val.append( float(fobj(pob[i]))/float(aco) )
	return val

def linRank(pob,Mu):
	MAX= 1.1 
	Mu = len(pob)/Mu
	val={}
	aux=[]
	proba=[]
	aco=0
	for i in xrange (0,len(pob)):
		aux.append([fobj(pob[i]),i])
	aux.sort(reverse=True)
	print aux
	#la lista se recorde con un ORDEN DECRECIENTE entonces val tendra tambien 
	# las calificaciones en ese orden 
	for i in xrange(0,len(pob)):
		if (i<Mu):
			f=2.0-MAX+ 2.0*(MAX-1.0)*( (float(aux[i][1])-1.0)/(Mu-1.0) )
		else:
			f=0		
		val[aux[i][1]]=f
	#ordenar las calificacion segun el orde de la poblacion
	for i in xrange(0,len(pob)):
		proba.append(val[i])
	return proba
	 
#----------------------- seleccion -------------------------------

def selec(cal):
	sumCal = 0
	calAcom=0
	res = [0,0]
	for j in xrange(0,2):

		for k in xrange(0,len(cal)):
			sumCal += cal[k]
		rand = random.random()*sumCal
		i=0
		while(i<len(cal) and calAcom<rand ):
			calAcom += cal[i]
			i+=1
		res[j]=i-1
	return res
	
	
#-------------------------- Mezclar ------------------------------

def mezclar(Can1, Can2):
	canMez1 =Can1
	canMez2 =Can2
	nvar=len(Can1)
	preci=len(Can1[0])
	if 0 == 0 :
		ind=random.randint(0,(preci)*nvar-1)
		for i in xrange(0,nvar):
			for j in xrange(0,preci):
				if(i*preci+j)<ind :
					canMez1[i][j] =Can2[i][j]
				else:
					canMez2[i][j]=Can1[i][j]
	return canMez1,canMez2
		
#---------------------------- Mutar ------------------------------

def main():
	NIND =40
	MAXGE = 300
	NVAR = 20
	PRECI= 20
	GGAP = 0.90
	
	# seleccionar poblacion inicial 
	
	pob=PoInAl(NIND, NVAR, PRECI)
	gen = 0 
	while(gen<MAXGE):
		newPob=[]
		
		for i in xrange(0,NVAR):
			calificacion = cal(pob)
			can1,can2=selec(calificacion)
			canM1,canM2=mezclar(pob[can1],pob[can2])
			newPob.append(canM1)
			newPob.append(canM2)
		pob=newPob
		gen+=1
	for i in xrange(0,NVAR):
		print fobj(pob[i])
#main()

"""
print dCodBin("00011")
a= PoInAl(5,2,5)

print a

for i in xrange(0,5):
	print fobj(a[i])
print "calificaciones "
c =linRank(a,2)
print c
can1,can2=selec(c)
print can1,can2
print mezclar(a[can1],a[can2])
"""

