#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from pprint import pprint
import numpy as np
import matplotlib.pyplot as plt


with open('PorcentajesAciertos.json') as data_file:    
    data = json.load(data_file)

#numero de aciertos por carpeta Prueba
def NumeroAciertosP(NumeroAciertos,metodo):

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
def NumeroAciertosP(NumeroAciertos,color='-hb',level = ""):

	NumeroProfundidad = [l for l in xrange(2,len(NumeroAciertos)+2)]
	a=NumeroAciertos
	a= [float(i)/30.0 for i in a ]
	print a
	#plt.plot(NumeroProfundidad,a , color,linewidth = 3, label = level )
	return a


	#plt.plot([1]+NumeroProfundidad, [.9,.9, .9, .9, .9, .9, .9, .9, .9, .9], '--k',linewidth = 1 )
def NumeroAciertosMMP(metodo,color='-hb',level = "") :	

	MAX = data["Comparacion"]["LE"][metodo][0][:]
	MIN = data["Comparacion"]["LE"][metodo][0][:]
	PRO = [ k-k for k in MIN ]

	for x in data["Comparacion"]["E"][metodo] :
		for y in xrange(0,len(x)):
			PRO[y]+=x[y]
			if MAX[y] < x[y]:
				MAX[y] = x[y]
			if MIN[y] > x[y]:
				MIN[y] = x[y]
	PRO = [float(i)/8 for i in PRO ]

	#for Narchivo in data["Comparacion"]["LE"][metodo]:
	#	NumeroAciertosP(Narchivo,'-hb')

	return NumeroAciertosP(PRO,color,level)
	#NumeroAciertosP(MAX,color,level)
	#NumeroAciertosP(MIN,color,level)


NumeroAciertosMMP("F",'-hb','Promedio FULL')
NumeroAciertosMMP("G",'-hg','Promedio GROW')
NumeroAciertosMMP("H",'-hr','Promedio Half and half')

N = 9
ind = ind = np.arange(N) 
width = 0.3      # the width of the bars
fig, ax = plt.subplots()

FULL = tuple(NumeroAciertosMMP("F",'-hb','Promedio FULL'))
rects1 = ax.bar(ind, FULL, width, color='b')

GROW = tuple(NumeroAciertosMMP("G",'-hg','Promedio GROW'))
rects2 = ax.bar(ind + width, GROW, width, color='g')

HALF = tuple(NumeroAciertosMMP("H",'-hr','Promedio Half and half'))
rects3 = ax.bar(ind + width+width, GROW, width, color='r')



# add some text for labels, title and axes ticks
ax.set_ylabel('Porcentaje de aciertos')
ax.set_xlabel('profundidad')
ax.set_xticks(ind + width+width)
ax.set_xticklabels(( '2', '3', '4', '5','6','7','8','9','10'))
plt.ylim(0,1.3)

ax.legend((rects1[0], rects2[0],rects3[0]), ('FULL', 'GROW', 'HALF AND HALF'))


def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1*height,'%.3f ' % round(height,3),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)

plt.show()