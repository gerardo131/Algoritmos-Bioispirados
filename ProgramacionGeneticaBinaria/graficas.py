import json
from pprint import pprint
import numpy as np
import matplotlib.pyplot as plt

with open('salidaHalfaAndHalf.json') as data_file:    
    data = json.load(data_file)

print data["Salida"][0]["Prueba"][0]["Generacion"][0]["Poblacion"][0]["Len"]


y=[]
x=[]

yM = []
xM = []
indx = 0

for i in data["Salida"][7]["Prueba"][0]["Generacion"] :
	for  j  in i["Poblacion"]:
	 	y.append(j["Len"])
	 	x.append(indx)
	 	if j["Error"] == '0.0' :
	 		yM.append(j["Len"])
	 		xM.append(indx)
	indx+=1





plt.plot(x, y, 'go')
plt.plot(xM, yM, 'ro')

plt.margins(0.2)
plt.subplots_adjust(bottom=0.15)
plt.xlabel('Generacion')
plt.ylabel('Tamano de Exprecion')
plt.show()