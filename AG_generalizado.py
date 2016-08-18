import math
from operator import xor
import random
import numpy as np
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
			fen=codBin(  random.randint (-5,5),preci)
			ind.append(fen)
		pob.append(ind)
	return pob
#------------------ funcion objetivo ----------------------------
"""
	#------------ funcion cuadratica --------------- 
def fobj(x):
	res=0
	res= -1*(dCodBin(x[0])-3)**2 + 100
	return res
"""
	#------------ funcion Ackley's -----------------
def fobj(X):
	var=[]
	for i in xrange(0,len(X)):
		var.append( float(dCodBin(X[i])) )
	
	res=0
	preres = -np.exp(0.5*(np.cos(2.0*np.pi*var[0])+np.cos(2.0*np.pi*var[1]) ) )+np.exp(1)+20.0
	res= -20.0*np.exp( -0.2*np.sqrt(0.5*(var[0]**2+var[1]**2) ) ) + preres
	return res

def adap(X,fmax,fmin):
	return fmax + fmin - fobj(X)

def adapMaxMin(pob):
	aux =[]
	for i in xrange(0,len(pob)):
		aux.append(fobj(pob[i]))
	return max(aux),min(aux)

#-------------------- Calificacion ----------------------------- 

def cal(pob): 
	val=[]
	aco=0
	fmax,fmin = adapMaxMin(pob)
	print "#-----------"
	for i in xrange(0,len(pob)):
		aco+=adap(pob[i],fmax,fmin)
		print str(adap(pob[i],fmax,fmin) ) +"  "+str(fobj(pob[i])) +"  "+ str(dCodBin(pob[i][0])) +"  "+ str(dCodBin(pob[i][1])) 
	print "----------------"
	for i in xrange(0,len(pob) ):
		val.append( float(adap(pob[i],fmax,fmin))/float(aco) )
	return val

def linRank(pob,Mu):
	MAX= 1.1 
	Mu = len(pob)/2
	val={} 	 	
	aux=[]
	proba=[]
	aco=0.0
	for i in xrange (0,len(pob)):
		aux.append([fobj(pob[i]),i])
	aux.sort(reverse=True)
	print aux
	#la lista se recorde con un ORDEN DECRECIENTE entonces val tendra tambien 
	# las calificaciones en ese orden 
	for i in xrange(0,len(pob)):
		if (i<krtfMu):
			f=2.0-MAX+ 2.0*(MAX-1.0)*( (float(i)-1.0)/(len(pob)-1.0) )
		else:
			f=0		
		val[aux[i][1]]=f
	#ordenar las calificacion segun el orde de la poblacion
	for i in xrange(0,len(pob)):
		proba.append(val[i])
	return proba



#----------------------- seleccion -------------------------------

def selec(cal,pob):
	sumCal = 0
	calAcom=0
	res = [0,0]
	for j in xrange(0,2):
		for k in xrange(0,len(cal)):
			sumCal += cal[k]
		r =random.random()
		rand = r*sumCal
		i=0
		while(i<len(cal) and calAcom<rand ):
			calAcom += cal[i]
			i+=1
		if i!=0 :
			res[j]=i-1
	print "generacion"
	print res
	print "----------"
	return res
	
	
#-------------------------- Mezclar ------------------------------

def mezclar(Can1, Can2):
	canMez1 =Can1
	canMez2 =Can2

	nvar=len(Can1)
	preci=len(Can1[0])
	if random.randint(0,1) == 0 :
		ind=random.randint(0,(preci)*nvar-1)
		for i in xrange(0,nvar):
			for j in xrange(0,preci):
				if(i*preci+j)<ind :
					canMez1[i][j] =Can2[i][j]
				else:
					canMez2[i][j]=Can1[i][j]
	return canMez1,canMez2
		
#---------------------------- Mutar ------------------------------
def mutacion (pob):
	for i in xrange(0, len(pob)) :
		if random.randint(0,1) == 0 :
			pob[ random.randint(0,len(pob)-1) ][random.randint(0,len(pob[0])-1)]
	return pob


def main():
	NIND =100
	MAXGE = 500
	NVAR = 2
	PRECI= 3
	
	# seleccionar poblacion inicial 
	
	pob=PoInAl(NIND, NVAR, PRECI)

	gen = 0 
	while(gen<MAXGE):
		newPob=[]
		
		for i in xrange(0,NIND/2):
			calificacion = cal(pob)
			can1,can2=selec(calificacion,pob)
			canM1,canM2=mezclar(pob[can1],pob[can2])
			newPob.append(canM1)
			newPob.append(canM2)
		pob=newPob
		pob=mutacion(pob)
		gen+=1
	max=0
	ind=0
	fmax,fmin = adapMaxMin(pob)
	for i in xrange(0,NIND):
		if max <adap(pob[i],fmax,fmin) :
			max = adap(pob[i],fmax,fmin)
			ind=i
	print " f("+ str(dCodBin(pob[ind][0]) ) +","+str(dCodBin(pob[ind][1]) )+") = " +str(fobj(pob[ind])) 
	print len(pob)
main()
#print fobj(["11","11"])
#print codBin(8,3)