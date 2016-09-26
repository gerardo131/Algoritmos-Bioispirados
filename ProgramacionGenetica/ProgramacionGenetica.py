import math
import random
import numpy as np
import matplotlib.pyplot as plt

import Individuo
import Calificacion
import PoblacionInicial
import Posfija
import seleccion 

def genMuestra(n = 2):
	muestraA =[]
	muestraR = []
	for i in xrange(0,n):
		a = random.random()*2.0-1.0
		r = a**2+a+1.0
		muestraA.append([a])
		muestraR.append(r)
	return [muestraA,muestraR]

def main():
	muestra = genMuestra(200)
	Pob = PoblacionInicial.aleatorio(4,2)
	Calificacion.adaptacion(Pob,muestra[0],muestra[1])
	plot=[]
	for i in Pob:
		print i.gen
		print i.calificacion
		res = []
		for x in muestra[0]:
			res.append(Posfija.evaluar(i.gen,x))
		plot.append(res)
	sel = seleccion.ruleta(Pob)
	for i in sel:
		print i.gen 
	

	plt.plot(muestra[0], muestra[1], 'ro')
	plt.plot(muestra[0], plot[0], 'go')
	plt.plot(muestra[0], plot[1], 'bo')
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