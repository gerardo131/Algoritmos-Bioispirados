#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from pprint import pprint
import numpy as np
import matplotlib.pyplot as plt


with open('PorcentajesAciertos.json') as data_file:    
    data = json.load(data_file)

#numero de aciertos por carpeta Prueba
def NumeroAciertosP(NumeroAciertos):

	NumeroProfundidad = [l for l in xrange(2,len(NumeroAciertos[0])+2)]
	a=NumeroAciertos[0]
	b=NumeroAciertos[1]
	c=NumeroAciertos[2]

	a= [float(i)/30.0 for i in a ]
	b= [float(i)/30.0 for i in b ]
	c= [float(i)/30.0 for i in c ]
	plt.plot(NumeroProfundidad,a , '-hb',linewidth = 3, label = 'FULL')
	plt.plot(NumeroProfundidad,b , '-hg',linewidth = 3, label = 'GROW')
	plt.plot(NumeroProfundidad,c , '-hr',linewidth = 3, label = 'HALF AND HALF')
	
	plt.plot([1]+NumeroProfundidad, [.9,.9, .9, .9, .9, .9, .9, .9, .9, .9], '--k',linewidth = 1 )
		
#numero de aciertos por Metodo 
def NumeroAciertosP(NumeroAciertos,color='-hb'):

	NumeroProfundidad = [l for l in xrange(2,len(NumeroAciertos)+2)]
	a=NumeroAciertos
	a= [float(i)/30.0 for i in a ]
	print a
	plt.plot(NumeroProfundidad,a , color,linewidth = 3)#, label = 'FULL')
	plt.plot([1]+NumeroProfundidad, [.9,.9, .9, .9, .9, .9, .9, .9, .9, .9], '--k',linewidth = 1 )
	

MAX = data["Comparacion"]["LE"]["G"][0][:]
MIN = data["Comparacion"]["LE"]["G"][0][:]
for x in data["Comparacion"]["LE"]["G"] :
	for y in xrange(0,len(x)):
		if MAX[y] < x[y]:
			MAX[y] = x[y]
		if MIN[y] > x[y]:
			MIN[y] = x[y]


for Narchivo in data["Comparacion"]["LE"]["G"]:
	NumeroAciertosP(Narchivo,'-hb')


NumeroAciertosP(MAX,'-hr')
NumeroAciertosP(MIN,'-hr')	

plt.margins(0.2)
plt.subplots_adjust(bottom=0.15)
plt.xlabel(u'profundidad')
plt.ylabel(u'Número de aciertos')
plt.legend()  # Creamos la caja con la leyenda
plt.minorticks_on()
plt.ylim(0,1.3)


plt.grid(True)
plt.show()