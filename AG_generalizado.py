import math
from operator import xor
import random
import numpy as np

import Mezcla
import Seleccion

import matplotlib.pyplot as plt

#---------------- Codificacion ---------------------------------
UMIN =[-31]#[-15,-3]
UMAX =[31]#[-5,3]
PRECI = 20
x = []
y = []
xM = []
yM = []
xMR = []
yMR = []

def codBin(num,k=0):
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
	
def dCodBin(Bin,k=0):
	global UMAX
	global UMIN
	global PRECI

	Inter =UMAX[k]-UMIN[k]
	bi=int(''.join(Bin),2)
	num =( (float(bi)* float(Inter))/float(2**(PRECI)-1.0)+UMIN[k]  )
	return num 

def dcodGenotipo(X):
	var = []
	if len(UMAX)==1 :
		for i in xrange(0,len(X)):
			var.append( float(dCodBin(X[i])) )
	else :
		for i in xrange(0,len(X)):
			var.append( float(dCodBin(X[i],i)) )
	return var

#--------------------- Poblacion inicial ------------------------
def PoInAl(nind, nvar):
	global UMAX
	global UMIN
	global PRECI

	pob=[]
	for i in xrange(0,nind):
		ind =[]
		for j in xrange(0,nvar):
			if len(UMAX)==1:
				fen=codBin(  random.randrange(UMIN[0],UMAX[0]))
			else:
				fen=codBin(  random.randrange(UMIN[j],UMAX[j]))
			ind.append(fen)
		pob.append(ind)
	return pob

#ordena la poblacion en funcion de la calificacion de cada genotipo 
def ordenar (cal,pob):
	var = []
	varC = []
	aux = []
	for i in xrange (0,len(pob)):
		aux.append([cal[i],i])
	aux.sort(reverse=True)
	for i in xrange (0,len(pob)):
		var.append(pob[aux[i][1]])
		varC.append( cal[aux[i][1]] )
	return var,varC

#----------------------- Seleccion -------------------------------
def selec(cal,pob):
	sumCal = 0
	
	res = [0,0]
	for j in xrange(0,2):
		calAcom=0
		for k in xrange(0,len(cal)):
			sumCal += cal[k]
		r = random.random()
		rand = r*sumCal
		i=0
		while(i<len(cal) and calAcom<rand ):
			calAcom += cal[i]
			i+=1
		if i!=0 :
			res[j]=i-1
	"""
	print "generacion"
	print res
	print "----------"
	"""
	return res
	
#---------------------------- Mutar ------------------------------
def mutacion (pob):
	for i in xrange(0, len(pob)) :
		if random.random()*10 < .2 :
			#print "----mutacion-----"
			for j in xrange(0,len(pob[i])):
				for k in xrange(0,len(pob[i][j])):
						if pob[i][j][k] == "1":
							pob[i][j][k] = "0"
						else:
							pob[i][j][k] = "1"
	return pob


def main():
	global UMAX
	global UMIN
	global PRECI
	global x
	global y
	global xM
	global xMR
	global yM
	global yMR
	
	NIND =100
	MAXGE = 1000
	NVAR = 8
	indEli=6
	
	# seleccionar poblacion inicial 
	pob=PoInAl(NIND, NVAR)
	
	gen = 0 
	while(gen<MAXGE):
		newPob=[]
		calificacion = cal(pob)
		maxfimp=0
		maxfimpin=0
		for i in xrange(0,len(pob)):
			print str(fobj(pob[i]))+"  "+str(dCodBin(pob[i][0]) ) + "  " +str(dCodBin(pob[i][1]) )
			if maxfimpin < calificacion[i]:
				maxfimp = calificacion[i]
				maxfimpin = i

		x.append(gen)
		y.append(fobj(pob[maxfimpin]))


		for i in xrange(0,(NIND-indEli)/2):
			can1,can2 = Seleccion.ruleta(calificacion,pob)
			"""
			print str(can1) +"   "+str(can2) 
			print "Mezclar : " 
			print "candidato uno"
			for i in xrange(0,NVAR):
				print str(dCodBin(pob[can1][i]) ) 
			print "candidato dos"
			for i in xrange(0,NVAR):
				print str(dCodBin(pob[can2][i]) ) 
			print "----------------------------------"
			"""
			canM1,canM2=Mezcla.puntos(pob[can1],pob[can2])

			xM.append(gen)
			xMR.append(gen)
			yM.append(fobj(pob[can1]))
			yMR.append(fobj(pob[maxfimpin]))

			xM.append(gen)
			xMR.append(gen)
			yM.append(fobj(canM1))
			yMR.append(fobj(canM2))

			newPob.append(canM1)
			newPob.append(canM2)

		newPob = mutacion(newPob)
		pob,calificacion =ordenar(calificacion,pob)
		# seleccion elitista
		for i in xrange(0,indEli):
			newPob.append(pob[i])
			print str(dCodBin(pob[i][0])) +"  "+str(dCodBin(pob[i][1]))
		#-----------------------------

		pob = newPob
		gen+=1
	max=0
	ind=0
	fmax,fmin,pp = adapMaxMin(pob)
	for i in xrange(0,len(pob)):
		if max <adap(pob[i],fmax,fmin) :
			max = adap(pob[i],fmax,fmin)
			ind=i
	print " f(x) = " +str(fobj(pob[ind]))
	print "x = "
	print dcodGenotipo(pob[ind])
	return fobj(pob[ind])

main()
#print fobj([-10.999818801707079, 1.2099592303840927])
#print codBin(8,3)
"""
funT =0
for i in xrange(0,10):
	funT += main() 
print funT/10.0

"""

"""
#prueba de funcion
for i in xrange(-15,-6): 
	for j in xrange(-3,4): 
		print str (fobj([i,j]) )+"  "+ str(i)+"  "+ str(j)
"""

#--------------- graficacion ---------
plt.plot(x, y, 'ro')
plt.plot(xM, yM, 'bo')
plt.plot(xMR, yMR, 'go')
plt.margins(0.2)
plt.subplots_adjust(bottom=0.15)
plt.show()


#-----------------purba de codificacion------------------
"""
for i in xrange(-5,5):
	print "-----------------------"
 	print i
 	a = codBin(i)
 	print dCodBin(a)
 	print "-----------------------"
"""