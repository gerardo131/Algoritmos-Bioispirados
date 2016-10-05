import math
import random
import numpy as np
import matplotlib.pyplot as plt
from operator import xor
import Individuo
import Calificacion
import PoblacionInicial
import seleccion 
import Mezcla
import Mutacion

def genMuestra(n = 1):
	muestraA =[]
	muestraR = []
	for i in xrange(0,n):
		a = [ random.randint(0,1) for x in xrange(0,3)]
		#print int(''.join(a), 2 )
		r = a[0]
		for i in xrange(1,len(a)) :
			r = xor(r, a[i])
		if  not(r) :
			r = 1
		else:
			r = 0

		muestraA.append(a)
		muestraR.append(r)
	return [muestraA,muestraR]

def ordenar (pob):
	var = []
	aux = []
	for i in xrange (0,len(pob)):
		aux.append([pob[i].calificacion,i])
	aux.sort(reverse=True)
	for i in xrange (0,len(pob)):
		var.append(pob[aux[i][1]])
	return var


def main(NIND = 8, MAXGE = 2 , NMUESTRA = 80, PROFUNDIDAD = 5 ,indEli =0,PC = 60,PM = 5):
	f=open("salida.txt","w") 
	"""
	NIND = 80
	MAXGE = 200
	NMUESTRA = 80
	PROFUNDIDAD = 5
	indEli = 4
	PC = 60
	PM = 2
	"""
	MaxFun =[]
	muestra = genMuestra(NMUESTRA)
	Pob = PoblacionInicial.aleatorio(NIND,PROFUNDIDAD)
	Calificacion.adaptacion(Pob,muestra[0],muestra[1])
	
	gen = 0
	while(gen<MAXGE):
		NuevaPob = []
		Pob = ordenar(Pob)
		for i in xrange(0,(NIND-indEli)/2):
			sel = seleccion.ruleta(Pob)
			ResMez = Mezcla.Punto(sel,PC)
			NuevaPob.append(ResMez[0])
			NuevaPob.append(ResMez[1])

		for i in xrange(0,NIND):
			MaxFun.append(Pob[i].error)

			"""
			print "----------- Seleccion -------------"
			print sel[0].gen
			print "             "
			print sel[1].gen
			print "------------ RES MEZCLA ---------"
			print ResMez[0].gen
			print "             "
			print ResMez[1].gen
			print "             "
			"""
		Mutacion.punto(NuevaPob,PROFUNDIDAD,PM)
	
		"""
		f.write( "------- POBLACION ---------  \n" )
		for i in Pob:
			f.write( str(i.calificacion)+"\n" )
			f.write( str(i.error)+"\n" )
		f.write( "------ END POBLACION ---------\n" )
		"""
	
		for i in xrange(0,indEli):
			NuevaPob.append(Pob[i])
		Pob = NuevaPob
		Calificacion.adaptacion(Pob,muestra[0],muestra[1])
		"""
		f.write( "--------- NUEVA POBLACION ---------\n" )
		for i in NuevaPob:
			f.write( str(i.gen)+"\n" )
			f.write( str(i.error) +"\n")
		f.write( "--------- END NUEVA POBLACION ---------\n" )
		"""
		#print "Terminar generacion"
		gen+=1
	f.close()
	


	#--------------------------- SALIDA IMPRECION/GRAFICACION ---------------------
	maximo = 0
	ind = 0 
	mini = 0
	indm = 0
	for i in xrange( 0,len(Pob) ):
		if Pob[i].calificacion > maximo:
			ind = i
			maximo = Pob[i].calificacion
		if Pob[i].calificacion < mini:
			indm = i
			mini = Pob[i].calificacion
	"""
	print Pob[ind].gen
	print Pob[ind].error
	print Pob[ind].calificacion
	print "----------------------------"
	print Pob[indm].gen
	print Pob[indm].error
	print Pob[indm].calificacion
	"""
	plot = []
	for i in muestra[0]:
		plot.append( Pob[ind].evaluar(i) )
	plotm = []
	for i in muestra[0]:
		plotm.append( Pob[indm].evaluar(i) )
	ejeX = []
	for i in xrange (0,MAXGE):
		for j in xrange (0, NIND):
			ejeX.append(i)	

	#plt.plot([i for i in xrange (0,NMUESTRA )], muestra[1], 'ro')
	#plt.plot([i for i in xrange (0,NMUESTRA )], plot, 'bo')
	plt.plot(ejeX, MaxFun, 'go')
	plt.margins(0.2)
	plt.subplots_adjust(bottom=0.15)
	plt.xlabel('Error')
	plt.ylabel('Generaciones')
	plt.show()
	#-------------------------------------------------------------------------------
	return Pob[ind]
main(NIND = 100 , MAXGE = 100 , NMUESTRA = 80, PROFUNDIDAD = 4 ,indEli =4,PC = 60,PM = 40)
"""
poMax = Individuo.Individuo(5)	
poMax.error = 80
PMa = 0

for x in xrange(0,100,5):
	i = main(NIND = 80, MAXGE = 200 , NMUESTRA = 80, PROFUNDIDAD = 5 ,indEli =4,PC = 60,PM = 5)
	print i.gen
	print "Error : "+str(i.error) 
	print "Pro Mutacion : " + str(PMa)
	if i.error< poMax.error:
		poMax = i
		PMa = x
print "----------- EL GANADOR ES -------------"
print poMax.gen
print "Error : "+str(poMax.error)
print "Pro Mutacion : " + str(PMa)
print "---------------------------------------"
