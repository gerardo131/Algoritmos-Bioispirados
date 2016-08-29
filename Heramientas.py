import 

#ordena la poblacion en funcion de la calificacion de cada genotipo 
def ordenar (cal,pob):
	var = []
	varC = []
	aux = []
	for i in xrange (0,len(pob)):
		aux.append([cal[i],i])
	aux.sort(reverse=True)
	for i in xrange (0,len(pob)):
		var.append(pob[aux[i][1]])
		varC.append( cal[aux[i][1]] )
	return var,varC