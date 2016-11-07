import math
import random
import numpy as np
import matplotlib.pyplot as plt
from operator import xor

import Individuo
import Calificacion
import PoblacionInicial
import seleccion 
import Mezcla
import Mutacion
 


def genMuestra(n = 1):
	muestraA =[]
	muestraR = []
	for i in xrange(0,n):
		#a = [ random.randint(0,1) for x in xrange(0,3)]
		aux = [ j-j for j in xrange( 0,Individuo.numVar-len(bin(i)[2:]) ) ] + list( bin(i)[2:] ) 
		a = [ int(j) for j in aux ]
		#print a

		#print int(''.join(a), 2 )
		r = a[0]
		for i in xrange(1,len(a)) :
			r = xor(r, a[i])
		if  not(r) :
			r = 1
		else:
			r = 0

		muestraA.append(a)
		muestraR.append(r)
	return [muestraA,muestraR]

def ordenar (pob):
	var = []
	aux = []
	for i in xrange (0,len(pob)):
		aux.append([pob[i].calificacion,i])
	aux.sort(reverse=True)
	for i in xrange (0,len(pob)):
		var.append(pob[aux[i][1]])
	return var

def ordenarTam(GenEli):
	var = []
	aux = []
	for i in xrange (0,len(GenEli)):
		aux.append([len(GenEli[i].gen),i])
	aux.sort()
	for i in xrange (0,len(GenEli)):
		var.append(GenEli[aux[i][1]])
	return var



def main(NIND = 1, MAXGE = 2 , NMUESTRA = 80, PROFUNDIDAD = 5 ,indEli =0,PC = 60,PM = 5):
	
	"""
	NIND = 80
	MAXGE = 200
	NMUESTRA = 80
	PROFUNDIDAD = 5
	indEli = 4
	PC = 60
	PM = 2
	"""
	MaxFun =[]
	MaxGen = []
	muestra = genMuestra(NMUESTRA)
	Pob = PoblacionInicial.aleatorio(NIND,PROFUNDIDAD)
	Calificacion.adaptacion(Pob,muestra[0],muestra[1])
	
	gen = 0

	f.write("{ \"Generacion\" :[" ) # ------------ JSON
	while(gen<MAXGE):

		NuevaPob = []

		for i in xrange(0,(NIND-(indEli)/2)/2):
			sel = seleccion.ruleta(Pob)
			ResMez = Mezcla.Punto(sel,PC)
			NuevaPob.append(ResMez[0])
			NuevaPob.append(ResMez[1])

		for i in xrange(0,NIND):
			MaxFun.append(Pob[i].error)

			"""
			print "----------- Seleccion -------------"
			print sel[0].gen
			print "             "
			print sel[1].gen
			print "------------ RES MEZCLA ---------"
			print ResMez[0].gen
			print "             "
			print ResMez[1].gen
			print "             "
			"""
		Mutacion.punto(NuevaPob,PROFUNDIDAD,PM)
		Pob = ordenar(Pob)
		#################### crear JSON  Poblacion ################################
		f.write("{ \"Poblacion\" :[" )
		for i in Pob[:len(Pob)-1]:
			f.write("{" )
		#	f.write("\"Gen\"  : \"" +  str(i.gen)+"\"  ,\n" )
			f.write("\"Cal\" : \"" + str(i.calificacion)+"\",\n" )
			f.write("\"Error\" : \"" + str(i.error)+"\",\n" )
			f.write("\"Len\" : \"" + str(len(i.gen))+"\"\n" )
			f.write("}," )

		f.write("{" )
		#f.write("\"Gen\"  : \"" +  str(Pob[len(Pob)-1].gen)+"\"  ,\n" )
		f.write("\"Cal\" : \"" + str(Pob[len(Pob)-1].calificacion)+"\",\n" )
		f.write("\"Error\" : \"" + str(Pob[len(Pob)-1].error)+"\",\n" )
		f.write("\"Len\" : \"" + str(len(Pob[len(Pob)-1].gen))+"\"\n" )
		f.write("}" )
		if gen < MAXGE-1: 
			f.write( "]}," )
		else:
			f.write( "]}" )
		###########################################################################

		MaxGen.append(Pob[0].error)
		GenEli = []

		for i in xrange(0,indEli):
			GenEli.append( Pob[i] )
		GenEli = ordenarTam( GenEli )

		for i in xrange(0,indEli/2):
			NuevaPob.append(GenEli[i])

		Pob = NuevaPob


		Calificacion.adaptacion(Pob,muestra[0],muestra[1])

		"""
		f.write( "--------- NUEVA POBLACION ---------\n" )
		for i in NuevaPob:
			f.write( str(i.gen)+"\n" )
			f.write( str(i.error) +"\n")
		f.write( "--------- END NUEVA POBLACION ---------\n" )
		"""
		#print "Terminar generacion"

		gen += 1

	f.write( "] }" ) #------------- JSON

	


	#--------------------------- SALIDA IMPRECION/GRAFICACION ---------------------
	# Buscando Mejor y peor resultado  
	maximo = 0
	ind = 0 
	mini = 0
	indm = 0
	for i in xrange( 0,len(Pob) ):
		if Pob[i].calificacion > maximo:
			ind = i
			maximo = Pob[i].calificacion
		elif Pob[i].calificacion == maximo and len(Pob[i].gen) < len(Pob[ind].gen):
			ind = i
			maximo = Pob[i].calificacion
		if Pob[i].calificacion < mini:
			indm = i
			mini = Pob[i].calificacion


	print "------------ Elitismos ----------------"
	for i in xrange( len(Pob)-4 ,len(Pob) ):
		print Pob[i].gen
		print Pob[i].error
	print "----------------------------------------"


	"""
	print Pob[ind].gen
	print Pob[ind].error
	print Pob[ind].calificacion
	print "----------------------------"
	print Pob[indm].gen
	print Pob[indm].error
	print Pob[indm].calificacion
	"""
	plot = []
	for i in muestra[0]:
		plot.append( Pob[ind].evaluar(i) )
	plotm = []
	for i in muestra[0]:
		plotm.append( Pob[indm].evaluar(i) )
	ejeX = []
	for i in xrange (0,MAXGE):
		for j in xrange (0, NIND):
			ejeX.append(i)	

	#plt.plot([i for i in xrange (0,NMUESTRA )], muestra[1], 'ro')
	plt.plot(ejeX, MaxFun, 'go')
	plt.plot([i for i in xrange (0,MAXGE )], MaxGen, 'ro')
	
	plt.margins(0.2)
	plt.subplots_adjust(bottom=0.15)
	plt.xlabel('Generaciones')
	plt.ylabel('Error')
	#plt.show()
	#-------------------------------------------------------------------------------
	return Pob[ind]
#main(NIND = 100 , MAXGE = 100 , NMUESTRA = 80, PROFUNDIDAD = 4 ,indEli =4,PC = 60,PM = 2)

poMax = Individuo.Individuo(5)	
poMax.error = 80
PMa = 0
iteracion = 10
for nArchivo in xrange(1,10):
	#f_latex=open("salida_latex.txt","w")
	f=open("Salida.json","w")
	f.write("{ \"Salida\" :[" ) # ------------ JSON
	for x in xrange(2,iteracion):
		f.write("{ \"Prueba\" :[" ) # ------------ JSON
		i = main(NIND = 80, MAXGE = 200 , NMUESTRA=8, PROFUNDIDAD = x  ,indEli=8 ,PC = 60,PM = 2)
		
		if x < iteracion-1: 
			f.write( "]}," )
		else:
			f.write( "]}" )

		print i.gen
		print "Error : "+str(i.error) 
		print "Pro Mutacion : " + str(PMa)

		############ guardar en archivo la salalida en formato latex ############
		stringGen = str(i.gen)
		#f_latex.write( " \item["+str(x)+"] "+ stringGen +"\n" )
		#f_latex.write( " Error :"+str(i.error)+"  \n" )
		#f_latex.write( " Len :"+ str( len(i.gen) ) +"  \n" )
		#######################################################################

		if i.error< poMax.error :
			poMax = i
			PMa = x
		elif i.error == poMax.error and len(i.gen) < len(poMax.gen):
			poMax = i
			PMa = x

	f.write( "]}" )# ------------ JSON



	print "----------- EL GANADOR ES -------------"
	print poMax.gen
	print "Error : "+str(poMax.error)
	print "Pro Mutacion : " + str(PMa)
	print "---------------------------------------"

	#f_latex.close()
	f.close()
