import math
from operator import xor
import random
import numpy as np
import matplotlib.pyplot as plt

#---------------- Representación ---------------------------------

x = []
y = []
xM = []
yM = []
xMR = []
yMR = []

def posfija(num,k=0):

def evalfuncion():
	

#--------------------- Poblacion inicial ------------------------
def PoInAl(nind, nvar):
	
#------------------ funcion objetivo ----------------------------


# funcion de adaptacion 
def adap(X,fmax,fmin):
	return fmax + fmin - fobj(X)

#busqueda de genotipo con valor de funcion objetivo maximo y minimo
def adapMaxMin(pob):
	aux =[]
	sumAux =0
	for i in xrange(0,len(pob)):
		aux.append(fobj(pob[i]))
		sumAux+=aux[i]
	return max(aux),min(aux),(sumAux/len(pob))

# buscar maximo y minimo de la funcion escalada
def MaxMin(pob,a,b):
	aux =[]
	for i in xrange(0,len(pob)):
		aux.append(escalado(fobj(pob[i]),a,b))
	return max(aux),min(aux)

#Encontrar los coeficientes de de la funcion escalada 
def preEscalar(umax,umin,uprom):
	fmultiple = 1.2
	delta = 0.0
	a=0.0
	b=0.0
	if umin >(fmultiple*uprom - umax)/(fmultiple-1.0): # prueba de no negatividad 
		# scala normal
		delta = umax- uprom+0.00001

		a=(fmultiple-1.0)*uprom/delta
		b=uprom*(umax - fmultiple*uprom)/delta
	else:
		delta = uprom- umin +0.00001
		a=uprom /delta
		b=-umin* uprom/ delta
	return a,b

#crear la funcion escalada
def escalado(f,a,b,):
	return a*f+b

#-------------------- Calificacion ----------------------------- 

def cal(pob): 
	val=[]
	aco=0
	fmax,fmin,pp = adapMaxMin(pob)
	a,b=preEscalar(fmax,fmin,pp)
	Emax,Emin = MaxMin(pob,a,b)
	for i in xrange(0,len(pob)):
		aco+=float( -escalado(fobj(pob[i]),a,b) +Emax+Emin )

	for i in xrange(0,len(pob) ):
		if aco ==0 :
			val.append(0.0)
		else:
			val.append( float( -escalado(fobj(pob[i]),a,b) +Emax+Emin )/float(aco) )
	return val

def simpleCal(pob):
	val=[]
	aco=0
	fmax,fmin,pp = adapMaxMin(pob)
	for i in xrange(0,len(pob)):
		aco+=adap(pob[i],fmax,fmin)
	for i in xrange(0,len(pob) ):
		if aco ==0 :
			val.append(0.0)
		else:
			val.append( float( adap(pob[i],fmax,fmin) )/float(aco) )
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

#----------------------- seleccion -------------------------------
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
	
#-------------------------- Mezclar ------------------------------
def mezclar(Can1, Can2):
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
	NVAR = 20
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
			can1,can2 = selec(calificacion,pob)
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
			canM1,canM2=mezclar(pob[can1],pob[can2])

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