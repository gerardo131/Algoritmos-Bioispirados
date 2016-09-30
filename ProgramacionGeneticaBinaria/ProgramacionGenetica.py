import math
import random
import numpy as np
import matplotlib.pyplot as plt

import Individuo
import Calificacion
import PoblacionInicial
import Posfija
import seleccion 
import Mezcla
import Mutacion

def genMuestra(n = 2):
	muestraA =[]
	muestraR = []
	for i in xrange(0,n):
		a = random.random()*2.0-1.0
		r = a**2+a+1.0
		muestraA.append([a])
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


def main():
	NIND = 80
	MAXGE = 200
	NMUESTRA = 200
	PROFUNDIDAD = 3
	indEli = 4

	muestra = genMuestra(NMUESTRA)
	Pob = PoblacionInicial.aleatorio(NIND,PROFUNDIDAD)
	Calificacion.adaptacion(Pob,muestra[0],muestra[1])
	gen = 0
	while(gen<MAXGE):
		NuevaPob = []

		for i in xrange(0,(NIND-indEli)/2):
			sel = seleccion.ruleta(Pob)
			ResMez = Mezcla.Punto(sel)
			NuevaPob.append(ResMez[0])
			NuevaPob.append(ResMez[1])
		print "nueva poblacion"
		for i in NuevaPob:
			print i.gen
		Mutacion.punto(NuevaPob,PROFUNDIDAD)
		Pob = ordenar(Pob)
		for i in xrange(0,indEli):
			NuevaPob.append(Pob[i])
		print "poblacion"
		for i in Pob:
			print i.calificacion
		print "---------------"
		Pob = NuevaPob
		Calificacion.adaptacion(Pob,muestra[0],muestra[1])


		print "Terminar generacion"
		gen+=1

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


	print Pob[ind].gen
	print Pob[ind].error
	plot = []
	for i in muestra[0]:
		plot.append( Posfija.evaluar(Pob[ind].gen,i) )
	plotm = []
	for i in muestra[0]:
		plotm.append( Posfija.evaluar(Pob[indm].gen,i) )

	plt.plot(muestra[0], muestra[1], 'ro')
	plt.plot(muestra[0], plot, 'bo')
	plt.plot(muestra[0], plotm, 'go')
	plt.margins(0.2)
	plt.subplots_adjust(bottom=0.15)
	plt.show()

	



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
"""
#--------------- graficacion ---------
plt.plot(x, y, 'ro')
plt.plot(xM, yM, 'bo')
plt.plot(xMR, yMR, 'go')
plt.margins(0.2)
plt.subplots_adjust(bottom=0.15)
plt.show()
"""

#-----------------purba de codificacion------------------
"""
for i in xrange(-5,5):
	print "-----------------------"
 	print i
 	a = codBin(i)
 	print dCodBin(a)
 	print "-----------------------"
"""