#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from pprint import pprint
import numpy as np
import matplotlib.pyplot as plt

def NumeroAciertos ():

	y=[]
	x=[]

	yMF = []
	xMF = []
	yPF=[]
	xPF=[]
	for  metodo in ['F','G','H'] :

		NumeroAciertos = [l-l for l in xrange(2,11)]
		NumeroProfundidad = [l for l in xrange(2,11)]

		for k in xrange(0,30):

<<<<<<< HEAD
			with open('Prueba2/Salida'+str(k)+metodo+'2_10.json') as data_file:    
=======
			with open('Prueba1/Salida'+str(k)+metodo+'2_10.json') as data_file:    
>>>>>>> bab6e09052ae1f401a1f65dfcc2ce468527c6772
			    data = json.load(data_file)

			#print data["Salida"][0]["Prueba"][0]["Generacion"][0]["Poblacion"][0]["Len"]

			############################ FULL ######################



			#for i in data["Salida"][profundidad]["Prueba"][0]["Generacion"] :
			for profundidad in xrange(0,len(data["Salida"])):
				i= data["Salida"][profundidad]["Prueba"][0]["Generacion"] [len(data["Salida"][profundidad]["Prueba"][0]["Generacion"])-1] # ultima generacion
				mejor = 80000
				peor  = 0
				for  j  in i["Poblacion"]:
				 	#y.append(j["Len"])
				 	#x.append(indx)
				 	#if j["Error"] == '0.0' :
			 		if j["Len"]=='6' and j["Error"] == '0.0':
			 			NumeroAciertos[profundidad] += 1
			 			break
			 			
			#plt.plot(xPF, yPF, 'r')
		if metodo == 'F':  
			plt.plot(NumeroProfundidad, NumeroAciertos, '-b',linewidth = 3, label = 'FULL')
			print "FULL"
			print NumeroAciertos
		elif metodo == 'G':
			plt.plot(NumeroProfundidad, NumeroAciertos, '-g',linewidth = 3, label = 'GROW')
			print "GROW"
			print NumeroAciertos
		elif metodo == 'H':
			plt.plot(NumeroProfundidad, NumeroAciertos, '-r',linewidth = 3, label = 'HALF AND HALF')
			print "HALF AND HALF"
			print NumeroAciertos

def NumeroAciertosP(O):
	NumeroProfundidad = [l for l in xrange(2,11)]
	if O == 'LE' :
		plt.plot(NumeroProfundidad, [24.0/30.0, 29.0/30.0, 28.0/30.0, 29.0/30.0, 28.0/30.0, 26.0/30.0, 14.0/30.0, 7.0/30.0, 7.0/30.0], '-hb',linewidth = 3, label = 'FULL')
		plt.plot(NumeroProfundidad, [14.0/30.0, 23.0/30.0, 30.0/30.0, 28.0/30.0, 28.0/30.0, 24.0/30.0, 19.0/30.0, 14.0/30.0, 9.0/30.0], '-hg',linewidth = 3, label = 'GROW')
		plt.plot(NumeroProfundidad, [7.0/30.0, 27.0/30.0, 29.0/30.0, 29.0/30.0, 25.0/30.0, 28.0/30.0, 22.0/30.0, 14.0/30.0, 8.0/30.0], '-hr',linewidth = 3, label = 'HALF AND HALF')
		
		plt.plot([1]+NumeroProfundidad, [.9,.9, .9, .9, .9, .9, .9, .9, .9, .9], '--k',linewidth = 1 )
		

	elif O == 'E':
		plt.plot(NumeroProfundidad, [24.0/30.0, 29.0/30.0, 28.0/30.0, 30.0/30.0, 30.0/30.0, 29.0/30.0, 30.0/30.0, 29.0/30.0, 30.0/30.0], '-hb',linewidth = 3, label = 'FULL')
		plt.plot(NumeroProfundidad, [14.0/30.0, 23.0/30.0, 30.0/30.0, 30.0/30.0, 30.0/30.0, 30.0/30.0, 29.0/30.0, 30.0/30.0, 30.0/30.0], '-hg',linewidth = 3, label = 'GROW')
		plt.plot(NumeroProfundidad, [7.0/30.0, 27.0/30.0, 29.0/30.0, 30.0/30.0, 29.0/30.0, 30.0/30.0, 30.0/30.0, 29.0/30.0, 30.0/30.0], '--hr',linewidth = 3, label = 'HALF AND HALF')
		plt.plot([1]+NumeroProfundidad, [.9,.9, .9, .9, .9, .9, .9, .9, .9, .9], '--k',linewidth = 1 )
		

#NumeroAciertos()
NumeroAciertosP('E')

<<<<<<< HEAD

	if O == 'LE' :
		a = [30, 30, 28, 29, 25, 23, 12, 8, 3]
		b = [12, 25, 30, 29, 25, 25, 16, 13, 7]
		c = [6, 27, 30, 28, 29, 26, 21, 16, 8]

		a= [float(i)/30.0 for i in a ]
		b= [float(i)/30.0 for i in b ]
		c= [float(i)/30.0 for i in c ]
		plt.plot(NumeroProfundidad,a , '-hb',linewidth = 3, label = 'FULL')
		plt.plot(NumeroProfundidad,b , '-hg',linewidth = 3, label = 'GROW')
		plt.plot(NumeroProfundidad,c , '-hr',linewidth = 3, label = 'HALF AND HALF')
		
		plt.plot([1]+NumeroProfundidad, [.9,.9, .9, .9, .9, .9, .9, .9, .9, .9], '--k',linewidth = 1 )
		

	elif O == 'E':
		a = [24.0, 29.0, 28.0, 30.0, 30.0, 29.0, 30.0, 29.0, 30.0]
		b = [14.0, 23.0, 30.0, 30.0, 30.0, 30.0, 29.0, 30.0, 30.0]
		C = [7.0, 27.0, 29.0, 30.0, 29.0, 30.0, 30.0, 29.0, 30.0]

		a= [float(i)/30.0 for i in a ]
		b= [float(i)/30.0 for i in b ]
		c= [float(i)/30.0 for i in c ]
		plt.plot(NumeroProfundidad, a, '-hb',linewidth = 3, label = 'FULL')
		plt.plot(NumeroProfundidad, b, '-hg',linewidth = 3, label = 'GROW')
		plt.plot(NumeroProfundidad, c, '--hr',linewidth = 3, label = 'HALF AND HALF')
		plt.plot([1]+NumeroProfundidad, [.9,.9, .9, .9, .9, .9, .9, .9, .9, .9], '--k',linewidth = 1 )



#NumeroAciertos()
NumeroAciertosP('LE')

=======
>>>>>>> bab6e09052ae1f401a1f65dfcc2ce468527c6772
"""
y=[]
x=[]
yMW = []
xMW = []
yPW=[]
xPW=[]
indx = 0
for i in dataG["Salida"][profundidad]["Prueba"][0]["Generacion"] :
	mejor = 80000
	peor  = 0
	for  j  in i["Poblacion"]:
	 	y.append(j["Len"])
	 	x.append(indx)
	 	if j["Error"] == '0.0' :
	 		if int(j["Len"]) < mejor:
	 			mejor = int(j["Len"])
	 		if int(j["Len"]) > peor :
	 			peor = int(j["Len"])
	if mejor != 80000 and peor != 0 :
		yMW.append(mejor)
		yPW.append(peor)
		xMW.append(indx)
		xPW.append(indx)
	indx+=1
#plt.plot(xPW, yPW, 'r')
plt.plot(xPW, yPW, 'r')
########################### halft and halft ########################
y=[]
x=[]
yMH = []
xMH = []
yPH=[]
xPH=[]
indx = 0
for i in dataH["Salida"][profundidad]["Prueba"][0]["Generacion"] :
	mejor = 80000
	peor  = 0
	for  j  in i["Poblacion"]:
	 	y.append(j["Len"])
	 	x.append(indx)
	 	#if j["Error"] == '0.0' :
 		if int(j["Len"]) < mejor:
 			mejor = int(j["Len"])
 		if int(j["Len"]) > peor :
 			peor = int(j["Len"])
	if mejor != 80000 and peor != 0 :
		yMH.append(mejor)
		yPH.append(peor)
		xMH.append(indx)
		xPH.append(indx)
	indx+=1
#plt.plot(xPH, yPH, 'r')
plt.plot(xPH, yPH, 'b')
"""
########################################################################
"""
FD = []
DEEP = []
for m  in ['F','G','H']:
	PD = []
	for deep in xrange(0,8):
		#print "-------------------------------"
		#print m+ str(deep)
		Asum = 0
		for w  in xrange(1,10):
			with open('Salida/Salida'+str(w)+m+'2_9.json') as data_file:    
			    data = json.load(data_file)
			Gene = data["Salida"][deep]["Prueba"][0]["Generacion"]
			sum = 0
			for i in Gene[len(Gene)-1]["Poblacion"] :
				if int(i["Len"])== 6 and float(i["Error"]) == 0.0:
						sum = 1
			Asum += sum
			#print sum 
		PD.append(Asum)
		#print "-------------------------------"
	FD.append(PD)	
	DEEP.append(deep+2)		
		
plt.plot([i for i in xrange(0,8)], FD[0], 'b')
plt.plot([i for i in xrange(0,8)], FD[1], 'g')
plt.plot([i for i in xrange(0,8)], FD[2], 'r')
"""
				



plt.margins(0.2)
plt.subplots_adjust(bottom=0.15)
plt.xlabel(u'profundidad')
plt.ylabel(u'Número de aciertos')
plt.legend()  # Creamos la caja con la leyenda
plt.minorticks_on()
plt.ylim(0,1.3)


plt.grid(True)
plt.show()