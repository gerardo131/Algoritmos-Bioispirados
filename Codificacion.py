import math
from operator import xor
import random
import numpy as np
UMIN =[-31]  #[-15,-3]
UMAX =[31]   #[-5,3]
PRECI = 20
tipo = "Binaria-PF"

# por defecto la codificacion sera binaria con puntos flotante

def Cod(num,k=0,t = ""): 
	if t == "Binaria-PF" or t == "":
		return codBinPF (num,k)

def Dcod(Bin ,k=0 , t = "" ):
	if t == "Binaria-PF" or t == "":
		return dCodBinPF (Bin,k)

def DcodGenotipo(X, t = ""):
	if t == "Binaria-PF" or t == "":
		return dCodBinPFGenotipo(X)
	

def codBinPF(num,k=0):
	global UMAX
	global UMIN
	global PRECI

	Inter = UMAX[k]-UMIN[k]
	binNum=""
	Bin=""
	binNum=bin(int( ( float(num-UMIN[k])*(2**(PRECI)-1.0 ) )/(Inter) ) )[2:]

	for i in xrange(0,PRECI-len(binNum)):
		Bin+="0"
	Bin += binNum
	return list(Bin)
	
def dCodBinPF(Bin,k=0):
	global UMAX
	global UMIN
	global PRECI

	Inter =UMAX[k]-UMIN[k]
	bi=int(''.join(Bin),2)
	num =( (float(bi)* float(Inter))/float(2**(PRECI)-1.0)+UMIN[k]  )
	return num 

def dCodBinPFGenotipo(X):
	var = []
	if len(UMAX)==1 :
		for i in xrange(0,len(X)):
			var.append( float(dCodBin(X[i])) )
	else :
		for i in xrange(0,len(X)):
			var.append( float(dCodBin(X[i],i)) )
	return var

def pruebas(a,b,t=""):
	for j in xrange (0,len(UMAX)):
		for i in xrange(a,b):
			print "#################################"
			print i
			print Cod(i,j,t)
			print Dcod(Cod(i,j),j,t)
			print "#################################"

pruebas(-31,31)
	
