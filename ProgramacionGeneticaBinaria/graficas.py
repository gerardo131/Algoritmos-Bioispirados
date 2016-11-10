#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from pprint import pprint
import numpy as np
import matplotlib.pyplot as plt

def NumeroAciertos (O,Narchivo):

	y=[]
	x=[]

	yMF = []
	xMF = []
	yPF=[]
	xPF=[]
	Salida = []
	for  metodo in ['F'] :

		NumeroAciertos = [l-l for l in xrange(2,11)]
		NumeroProfundidad = [l for l in xrange(2,11)]

		for k in xrange(0,30):

			with open('Prueba'+str(Narchivo)+'/Salida'+str(k)+metodo+'2_10.json') as data_file:    
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
				 	if O == 'LE' :
			 			if j["Len"]=='6' and j["Error"] == '0.0':
				 			NumeroAciertos[profundidad] += 1
				 			break
				 	elif O == 'E' :
			 			if j["Error"] == '0.0':
				 			NumeroAciertos[profundidad] += 1
				 			break
			 			
			#plt.plot(xPF, yPF, 'r')
		if metodo == 'F':  
			#plt.plot(NumeroProfundidad, NumeroAciertos, '-b',linewidth = 3, label = 'FULL')
			print "FULL"
			print NumeroAciertos
			Salida.append(NumeroAciertos)
		elif metodo == 'G':
			#plt.plot(NumeroProfundidad, NumeroAciertos, '-g',linewidth = 3, label = 'GROW')
			print "GROW"
			print NumeroAciertos
			Salida.append(NumeroAciertos)
		elif metodo == 'H':
			#plt.plot(NumeroProfundidad, NumeroAciertos, '-r',linewidth = 3, label = 'HALF AND HALF')
			print "HALF AND HALF"
			print NumeroAciertos
			Salida.append(NumeroAciertos)
	return Salida



prueba = 'E' #LE = comparar longitud y Error E = Error  
for Narchivo in xrange(1,9):
	NumeroAciertos(prueba,Narchivo)


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