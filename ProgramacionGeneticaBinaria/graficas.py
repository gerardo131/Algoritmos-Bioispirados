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
				bandera = 1
				indxPo = 0
				while (bandera and indxPo<len(i["Poblacion"]) ):
					j=i["Poblacion"][indxPo]
				 	#y.append(j["Len"])
				 	#x.append(indx)
				 	#if j["Error"] == '0.0' :
				 	if O == 'LE' :
			 			if j["Len"]=='6' and j["Error"] == '0.0':
				 			NumeroAciertos[profundidad] += 1
				 			bandera = 0
				 	elif O == 'E' :
			 			if j["Error"] == '0.0':
				 			NumeroAciertos[profundidad] += 1
				 			bandera = 0
				 	indxPo += 1
			 			
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

def Tiempo (Narchivo,metodo,color):

	yt = [ l-l for l in xrange(2,11) ]
	xt = [ l for l in xrange(2,11) ]
	
	for k in xrange(0,30):

		with open('Prueba'+str(Narchivo)+'/Salida'+str(k)+metodo+'2_10.json') as data_file:    
		    data = json.load(data_file)

		#print data["Salida"][0]["Prueba"][0]["Generacion"][0]["Poblacion"][0]["Len"]


		for i in xrange(0,len(data["Salida"])):
			#print i["Prueba"][0]["TiempoTotal"]
			yt[i]+=float (data["Salida"][i]["Prueba"][0]["TiempoTotal"])/30

	if metodo == 'F':  
		plt.plot(xt, yt, color,linewidth = 3, label = 'FULL')
	elif metodo == 'G':
		plt.plot(xt, yt, color,linewidth = 3, label =  'GROW')
	elif metodo == 'H':
		plt.plot(xt, yt, color,linewidth = 3, label =  'HALF AND HALF')

def  Distribucion (Narchivo,profundidad,k ,metodo,color):

	y=[]
	x=[]
	yC=[]
	xC=[]
	yB=[]
	xB=[]

	yM = []
	xM = []
	yP=[]
	xP=[]
	Salida = []

		

	
	
	with open('Prueba'+str(Narchivo)+'/Salida'+str(k)+metodo+'2_10.json') as data_file:    
	    data = json.load(data_file)

	#print data["Salida"][0]["Prueba"][0]["Generacion"][0]["Poblacion"][0]["Len"]
	yt = [ l-l for l in xrange(0,len(data["Salida"][profundidad]["Prueba"][0]["Generacion"])) ]
	xt = [ l for l in xrange(0,len(data["Salida"][profundidad]["Prueba"][0]["Generacion"])) ]

	indx=0
	for i in data["Salida"][profundidad]["Prueba"][0]["Generacion"] :
		mejor = 80000
		peor  = 0
		#print i["Prueba"][0]["TiempoTotal"]
		for  j  in i["Poblacion"]:
		 	y.append(j["Len"])
		 	x.append(indx)
		 	yt[indx] += float(j["Len"])/float(len(i["Poblacion"])) 

		 	if j["Error"] == '0.0' :
					yC.append(j["Len"])
		 			xC.append(indx)	
		 	if j["Error"] == '0.0' and j["Len"]=='6' :
					yB.append(j["Len"])
		 			xB.append(indx)	
	 		if int(j["Len"]) < mejor:
	 			mejor = int(j["Len"])
	 		if int(j["Len"]) > peor :
	 			peor = int(j["Len"])
		if mejor != 80000 and peor != 0 :
			yM.append(mejor)
			yP.append(peor)
			xM.append(indx)
			xP.append(indx)
		
		indx+=1



	if metodo == 'F':  
		print max(yP)
		plt.plot(x, y, 'ob',linewidth = 3, label = 'FULL')
		plt.plot(xP, yP, color,linewidth = 3, label = 'FULL')
		#plt.plot(xC, yC, 'or',linewidth = 3, label = 'FULL')
		#plt.plot(xt, yt, '-hc',linewidth = 3, label = 'FULL')
		#print yP
	elif metodo == 'G':
		print max(yP)
		plt.plot(x, y, 'og',linewidth = 3, label =  'GROW')
		plt.plot(xP, yP, color,linewidth = 3, label = 'GROW')
		#plt.plot(xt, yt, '-hc',linewidth = 3, label = 'FULL')
	elif metodo == 'H':
		print max(yP)
		print yP.index(max(yP))
		plt.plot(x, y, 'or',linewidth = 3, label =  'HALF AND HALF')
		plt.plot(xP, yP, color,linewidth = 3, label = 'HALF AND HALF')
		#plt.plot(xt, yt, '-hc',linewidth = 3, label = 'FULL')

	"""
	plt.margins(0.2)
	plt.subplots_adjust(bottom=0.15)
	plt.xlabel(u'Generación')
	plt.ylabel(u'Tamaño de expreción')
	plt.legend()  # Creamos la caja con la leyenda
	plt.minorticks_on()
	plt.xlim(-2,202)
	plt.savefig(metodo+"-Po"+str(profundidad)+"-Ma"+str(max(yP))+"-Ge"+str(yP.index(max(yP)))+".png" )
	plt.grid(True)
	plt.show()
	"""
	
def  DistribucionMax (Narchivo,profundidad,k ,metodo,color):
	y=[]
	x=[]
	yC=[]
	xC=[]
	yB=[]
	xB=[]

	yM = []
	xM = []
	yP=[]
	xP=[]
	Salida = []
	
	with open('Prueba'+str(Narchivo)+'/Salida'+str(k)+metodo+'2_10.json') as data_file:    
	    data = json.load(data_file)

	#print data["Salida"][0]["Prueba"][0]["Generacion"][0]["Poblacion"][0]["Len"]
	yt = [ l-l for l in xrange(0,len(data["Salida"][profundidad]["Prueba"][0]["Generacion"])) ]
	xt = [ l for l in xrange(0,len(data["Salida"][profundidad]["Prueba"][0]["Generacion"])) ]

	indx=0
	for i in data["Salida"][profundidad]["Prueba"][0]["Generacion"] :
		mejor = 80000
		peor  = 0
		#print i["Prueba"][0]["TiempoTotal"]
		for  j  in i["Poblacion"]:
		 	y.append(j["Len"])
		 	x.append(indx)
		 	yt[indx] += float(j["Len"])/float(len(i["Poblacion"])) 

		 	if j["Error"] == '0.0' :
					yC.append(j["Len"])
		 			xC.append(indx)	
		 	if j["Error"] == '0.0' and j["Len"]=='6' :
					yB.append(j["Len"])
		 			xB.append(indx)	
	 		if int(j["Len"]) < mejor:
	 			mejor = int(j["Len"])
	 		if int(j["Len"]) > peor :
	 			peor = int(j["Len"])
		if mejor != 80000 and peor != 0 :
			yM.append(mejor)
			yP.append(peor)
			xM.append(indx)
			xP.append(indx)
		
		indx+=1



	if metodo == 'F':  
		print max(yP)
		plt.plot(x, y, 'ob',linewidth = 3, label = 'FULL')
		plt.plot(xP, yP, color,linewidth = 3, label = 'FULL')
		#plt.plot(xC, yC, 'or',linewidth = 3, label = 'FULL')
		#plt.plot(xt, yt, '-hc',linewidth = 3, label = 'FULL')
		#print yP
	elif metodo == 'G':
		print max(yP)
		plt.plot(x, y, 'og',linewidth = 3, label =  'GROW')
		plt.plot(xP, yP, color,linewidth = 3, label = 'GROW')
		#plt.plot(xt, yt, '-hc',linewidth = 3, label = 'FULL')
	elif metodo == 'H':
		print max(yP)
		print yP.index(max(yP))
		plt.plot(x, y, 'or',linewidth = 3, label =  'HALF AND HALF')
		plt.plot(xP, yP, color,linewidth = 3, label = 'HALF AND HALF')
		#plt.plot(xt, yt, '-hc',linewidth = 3, label = 'FULL')



def  convergencia(Narchivo,metodo,color):

	yC = [ ]
	xC = [ ]
	yCB = []
	xCB = []

	yAP = [ l-l for l in xrange(2,11)]
	yIP = [ l-l for l in xrange(2,11)]
	xP = [ l for l in xrange(2,11) ]
	NP = [ [] for l in xrange(2,11)]

	yt = [ l-l for l in xrange(2,11) ]
	xt = [ l for l in xrange(2,11) ]
	Nt = [ l-l for l in xrange(2,11) ]

	for k in xrange(0,30):

		with open('Prueba'+str(Narchivo)+'/Salida'+str(k)+metodo+'2_10.json') as data_file:    
		    data = json.load(data_file)

		#print data["Salida"][0]["Prueba"][0]["Generacion"][0]["Poblacion"][0]["Len"]

		for profundidad in xrange(0,len(data["Salida"])):
			bandera = 1
			i=0
			while  bandera and i <len(data["Salida"][profundidad]["Prueba"][0]["Generacion"]) :
				gen = data["Salida"][profundidad]["Prueba"][0]["Generacion"][i]
				indxPo = 0
				while bandera and  indxPo<len(gen["Poblacion"]):
					j = gen["Poblacion"][indxPo]
					if j["Error"] == '0.0' and j['Len']=='6' and i<50:
						Nt[profundidad]+=1.0
						yt[profundidad]+=i
				 	if j["Error"] == '0.0' and  j['Len']=='6':
				 		bandera = 0
				 		yC.append(i)
				 		xC.append(profundidad+2)
				 		NP[profundidad].append(i)
				 	indxPo +=1
				i+=1
			if bandera  :
				print 'Prueba'+str(Narchivo)+'/Salida'+str(k)+metodo+str(profundidad)


	for NPi in xrange(0,len(NP)):
		NP[NPi].sort()
		aux = NP[NPi][0: int(float(len(NP[NPi]))*.9 )]
		yAP[NPi] = max(aux)
		yIP[NPi] = min(aux)			

	if metodo == 'F':  
		#xPM =[ l-l for l in xrange(2,11) ]
		#yPM = [ l for l in xrange(2,11) ]

		#for arrpuni in xrange(0,len(NP)):
		#	arrpun = NP[arrpuni]
		#	for punto in xrange(0,len(arrpun)):
		#		xPM[arrpuni]+=float(arrpun[punto])/float(len(arrpun) )
		#	print xPM[arrpuni]

		#plt.plot(xC, yC, 'ob',linewidth = 3, label = 'FULL')
		#plt.plot(yPM, xPM, '-hb',linewidth = 3, label =  'FULL')
		##plt.plot(xt, yt, color,linewidth = 3, label = 'FULL')
		#aux1 =[]
		#for x in NP:
		#	aux1 = aux1+[x]+[[]]+[[]]

		plt.boxplot(NP, sym = 'ko', whis = 1.5,flierprops = dict(marker='o', markerfacecolor='blue'),boxprops = dict( color='blue') )
		#plt.xticks([ (l*3)+1 for l in xrange(0,9) ], xP, size = 'small', color = 'b')
		#plt.plot(xP, yAP, color,linewidth = 3, label = 'FULL')
		#plt.plot(xP, yIP, color,linewidth = 3, label = 'FULL')
	elif metodo == 'G':
		#xPM =[ l-l for l in xrange(2,11) ]
		#yPM = [ l for l in xrange(2,11) ]

		#for arrpuni in xrange(0,len(NP)):
		#	arrpun = NP[arrpuni]
		#	for punto in xrange(0,len(arrpun)):
		#		xPM[arrpuni]+=float(arrpun[punto])/float(len(arrpun) )
		#	print xPM[arrpuni]

		#plt.plot(xC, yC, 'ob',linewidth = 3, label =  'GROW')
		#plt.plot(yPM, xPM, '-hg',linewidth = 3, label =  'GROW')
		##plt.plot(xt, yt, color,linewidth = 3, label = 'FULL')
		#aux1 =[]
		#for x in NP:
		#	aux1 = aux1+[[]]+[x]+[[]]
		plt.boxplot(NP, sym = 'ko', whis = 1.5, flierprops = dict(marker='o', markerfacecolor='green'),boxprops = dict( color='green'))
		#plt.xticks([ (l*3)+2 for l in xrange(0,9) ], xP, size = 'small', color = 'g')
		#plt.plot(xP, yAP, color,linewidth = 3, label = 'FULL')
		#plt.plot(xP, yIP, color,linewidth = 3, label = 'FULL')
	elif metodo == 'H':
		#xPM =[ l-l for l in xrange(2,11) ]
		#yPM = [ l for l in xrange(2,11) ]

		#for arrpuni in xrange(0,len(NP)):
		#	arrpun = NP[arrpuni]
		#	for punto in xrange(0,len(arrpun)):
		#		xPM[arrpuni]+=float(arrpun[punto])/float(len(arrpun) )
		#	print xPM[arrpuni]
	
		#plt.plot(xC, yC, 'or',linewidth = 3, label =  'HALF AND HALF')
		#plt.plot(yPM, xPM, '-hr',linewidth = 3, label =  'HALF AND HALF')
		##plt.plot(xt, yt, color,linewidth = 3, label = 'FULL')
		#aux1 =[]
		#for x in NP:
		#	aux1 = aux1+[[]]+[[]]+[x]
		plt.boxplot(NP, sym = 'ko', whis = 1.5, flierprops = dict(marker='o', markerfacecolor='red'),boxprops = dict( color='red') )
		#plt.xticks(xP, xP, size = 'small', color = 'r')
		#plt.plot(xP, yAP, color,linewidth = 3, label = 'FULL')
		#plt.plot(xP, yIP, color,linewidth = 3, label = 'FULL')





print "iniciando"
#--------------------TIEMPOS DE EJECUCION---------------------------------------
#Tiempo(5,"F",'-hb')
#Tiempo(5,"H",'-hr')
#Tiempo(5,"G",'-hg')

#Tiempo(4,"H",'-c')
#Tiempo(5,"H",'-m')
#Tiempo(6,"H",'-k')
#Tiempo(7,"H",'-y')
#Tiempo(8,"H",'-b')
#--------------------------------------------------------------------------------

#-----------------------Distribucion--------------------------------------
#for  arp in xrange(3,4):
#	for arcin in xrange(0,30):
#		Distribucion(arp,1,arcin,"F",'ob')
for rap in xrange(0,9):
	print rap
	Distribucion(2,rap,20,"G",'oy')
	print "   "
#Distribucion(5,1,20,"F",'or')
#Distribucion(5,1,20,"G",'or')
#Distribucion(2,1,20,"H",'og')
#Distribucion(1,"H",,'or')
#-------------------------------------------------------------------------

#------------------- MINIMA GENERACION DE CONVERGENCIA --------------------
#convergencia(2,"H",'-hy')
#convergencia(2,"F",'-hc')
#convergencia(3,"G",'-hm')
#convergencia(4,"H",'-hk')
#convergencia(5,"H",'-hr')
#convergencia(6,"H",'-hg')
#convergencia(7,"H",'--y')
#convergencia(8,"H",'--c')


#--------------------------------------------------------------------------

#------------------ Aciertos-----------------------------------------------------
#prueba = 'E' #LE = comparar longitud y Error E = Error  
#for Narchivo in xrange(1,9):
#	NumeroAciertos(prueba,Narchivo)


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
				


