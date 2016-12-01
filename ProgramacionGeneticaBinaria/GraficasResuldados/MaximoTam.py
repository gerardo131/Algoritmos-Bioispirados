#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

"""
F-Po0-Ma27-Ge92,
F-Po1-Ma45-Ge29,  
F-Po2-Ma83-Ge10, 
F-Po3-Ma126-Ge38,
F-Po4-Ma204-Ge14,
F-Po5-Ma373-Ge4,  
F-Po6-Ma406-Ge18,  
F-Po7-Ma601-Ge0,   
F-Po8-Ma1143-Ge4,

G-Po0-Ma29-Ge29,  
G-Po1-Ma29-Ge6, 
G-Po2-Ma54-Ge25, 
G-Po3-Ma84-Ge10,  
G-Po4-Ma113-Ge7, 
G-Po5-Ma327-Ge9, 
G-Po6-Ma361-Ge0,
G-Po7-Ma693-Ge8, 
G-Po8-Ma1227-Ge2,

H-Po0-Ma40-Ge21,
H-Po1-Ma33-Ge3,  
H-Po2-Ma56-Ge20,   
H-Po3-Ma78-Ge17,  
H-Po4-Ma142-Ge3, 
H-Po5-Ma212-Ge1, 
H-Po6-Ma425-Ge2, 
H-Po7-Ma636-Ge13,  
H-Po8-Ma1146-Ge0,

[27,126,406,45,204,601,83,373,1143]

[29,84,361,29,113,693,54,327,1227]

[40,78,425,33,142,636,56,212,1146]

"""
#rects1 = ax.bar([2,3,4,5,6,7,8,9,10], [27,45,83,126,204,373,406,601,1143], width, color='r', yerr=menStd)
#plt.bar(, [27,45,83,126,204,373,406,601,1143])
#plt.hist([2,3,4,5,6,7,8,9,10], [29,29,54,84,113,327,361,693,1227], '-hg',linewidth = 3, label = 'GROW')
#plt.hist([2,3,4,5,6,7,8,9,10], [40,33,56,78,142,212,425,636,1146], '-hr',linewidth = 3, label = 'HALF AND HALF')
N = 9
ind = ind = np.arange(N) 
width = 0.3      # the width of the bars
fig, ax = plt.subplots()

FULL = (27,45,83,126,204,373,406,601,1143)
rects1 = ax.bar(ind, FULL, width, color='b')

GROW = (29,29,54,84,113,327,361,693,1227)
rects2 = ax.bar(ind + width, GROW, width, color='g')

HALF = (40,33,56,78,142,212,425,636,1146)
rects3 = ax.bar(ind + width+width, GROW, width, color='r')



# add some text for labels, title and axes ticks
ax.set_ylabel(u'Máxima longitud')
ax.set_title('Profundidad')
ax.set_xticks(ind + width+width)
ax.set_xticklabels(('2', '3', '4', '5','6','7','8','9','10'))

ax.legend((rects1[0], rects2[0],rects3[0]), ('FULL', 'GROW', 'HALF AND HALF'))


def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1*height,
                '%d' % int(height),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)

plt.show()