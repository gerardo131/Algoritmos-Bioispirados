#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from pprint import pprint
import numpy as np
import matplotlib.pyplot as plt
"""
Tomando una sola muestra que converge en cada profundidad

Concluciones 
	Las longitudes promedio mas altas se encunetran en el metodo FULL, esto nos es posible que si no se tiene 
    idea de la longitud  la la exprecion real el metodo FULL no sea el indicado para  encontrar la solución.



F-Prof 2
    -Max     34
    -MaxMedi 7.14141414141
    -Gene    103
    -GeneM   86
F-Prof 3
    -Max     44
    -MaxMedi 12.2323232323
    -Gene    11
    -GeneM   2
F-Prof 4
    -Max     65
    -MaxMedi 21.65
    -Gene    6
    -GeneM   0
F-Prof 5
    -Max     105
    -MaxMedi 36.1
    -Gene    21
    -GeneM   0
F-Prof 6
    -Max     165
    -MaxMedi 71.595959596
    -Gene    2
    -GeneM   1
F-Prof 7
    -Max     320
    -MaxMedi 132.161616162
    -Gene    5
    -GeneM   1
F-Prof 8
    -Max     502
    -MaxMedi 222.868686869
    -Gene    3
    -GeneM   1
F-Prof 9
    -Max     800
    -MaxMedi 386.696969697
    -Gene    33
    -GeneM   4
F-Prof 10
    -Max     1033
    -MaxMedi 672.686868687
    -Gene    2
    -GeneM   1

#################################################

G-Prof 2
    -Max     26
    -MaxMedi 7.19191919192
    -Gene    188
    -GeneM   155
G-Prof 3
    -Max     46
    -MaxMedi 9.57575757576
    -Gene    11
    -GeneM   12
G-Prof 4
    -Max     64
    -MaxMedi 19.2828282828
    -Gene    15
    -GeneM   5
G-Prof 5
    -Max     84
    -MaxMedi 31.2525252525
    -Gene    26
    -GeneM   13
G-Prof 6
    -Max     155
    -MaxMedi 53.9595959596
    -Gene    8
    -GeneM   5
G-Prof 7
    -Max     354
    -MaxMedi 114.565656566
    -Gene    10
    -GeneM   5
G-Prof 8
    -Max     450
    -MaxMedi 169.323232323
    -Gene    15
    -GeneM   13
G-Prof 9
    -Max     650
    -MaxMedi 310.424242424
    -Gene    19
    -GeneM   9
G-Prof 10
    -Max     1040
    -MaxMedi 353.686868687
    -Gene    0
    -GeneM   3

################################################

H-Prof 2
    -Max     35
    -MaxMedi 7.26262626263
    -Gene    121
    -GeneM   118
H-Prof 3
    -Max     40
    -MaxMedi 9.32
    -Gene    190
    -GeneM   0
H-Prof 4
    -Max     62
    -MaxMedi 17.61
    -Gene    19
    -GeneM   0
H-Prof 5
    -Max     84
    -MaxMedi 29.23
    -Gene    15
    -GeneM   0
H-Prof 6
    -Max     143
    -MaxMedi 58.9191919192
    -Gene    11
    -GeneM   1
H-Prof 7
    -Max     292
    -MaxMedi 91.79
    -Gene    7
    -GeneM   0
H-Prof 8
    -Max     364
    -MaxMedi 152.04
    -Gene    0
    -GeneM   0
H-Prof 9
    -Max     636
    -MaxMedi 288.404040404
    -Gene    13
    -GeneM   1
H-Prof 10
    -Max     1187
    -MaxMedi 497.505050505
    -Gene    1
    -GeneM   1
"""

#   (7.14141414141,12.2323232323,21.65,36.1,71.595959596,132.161616162,222.868686869,386.696969697,672.686868687)
#   (7.19191919192,9.57575757576,19.2828282828,31.2525252525,53.9595959596,114.565656566,169.323232323,310.424242424,353.686868687)
#   (7.26262626263,9.32,17.61,29.23,58.9191919192,91.79,152.04,288.404040404,497.50505050)

N = 9
ind = ind = np.arange(N) 
width = 0.3      # the width of the bars
fig, ax = plt.subplots()

FULL = (7.14141414141,12.2323232323,21.65,36.1,71.595959596,132.161616162,222.868686869,386.696969697,672.686868687)
rects1 = ax.bar(ind, FULL, width, color='b')

GROW = (7.19191919192,9.57575757576,19.2828282828,31.2525252525,53.9595959596,114.565656566,169.323232323,310.424242424,353.686868687)
rects2 = ax.bar(ind + width, GROW, width, color='g')

HALF = (7.26262626263,9.32,17.61,29.23,58.9191919192,91.79,152.04,288.404040404,497.50505050)
rects3 = ax.bar(ind + width+width, GROW, width, color='r')



# add some text for labels, title and axes ticks
ax.set_ylabel(u'longitud Promedio')
ax.set_title('Profundidad')
ax.set_xticks(ind + width+width)
ax.set_xticklabels(('2', '3', '4', '5','6','7','8','9','10'))
plt.ylim(0,780)
ax.legend((rects1[0], rects2[0],rects3[0]), ('FULL', 'GROW', 'HALF AND HALF'))


def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1*height,
                '%.1f' % height,
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)

plt.show()