import json
from pprint import pprint
import numpy as np
import matplotlib.pyplot as plt

with open('Salida/Salida7G2_9.json') as data_file:    
    dataF = json.load(data_file)

with open('Salida/Salida8G2_9.json') as data_file:    
    dataG = json.load(data_file)

with open('Salida/Salida9G2_9.json') as data_file:    
    dataH = json.load(data_file)

print dataF["Salida"][0]["Prueba"][0]["Generacion"][0]["Poblacion"][0]["Len"]
profundidad  = 7
############################ FULL ######################
y=[]
x=[]

yMF = []
xMF = []
yPF=[]
xPF=[]

indx = 0


for i in dataF["Salida"][profundidad]["Prueba"][0]["Generacion"] :
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
		yMF.append(mejor)
		yPF.append(peor)
		xMF.append(indx)
		xPF.append(indx)

	indx+=1
##plt.plot(xPF, yPF, 'r')
#plt.plot(xPF, yPF, 'g')

######################## GROW #################################

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
##plt.plot(xPW, yPW, 'r')
#plt.plot(xPW, yPW, 'r')

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
##plt.plot(xPH, yPH, 'r')
#plt.plot(xPH, yPH, 'b')

########################################################################
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
				if int(i["Len"])< 10 and float(i["Error"]) < 0.1:
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

			



plt.margins(0.2)
plt.subplots_adjust(bottom=0.15)
plt.xlabel('Generacion')
plt.ylabel('Tamano de Exprecion')

plt.grid(True)
plt.show()