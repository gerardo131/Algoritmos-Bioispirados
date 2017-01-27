import math
import random
import numpy as np
import matplotlib.pyplot as plt
from operator import xor
from time import time

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
		mu = [random.randint(0,80) for i in xrange(0,10)]
		muestraA.append(mu)
		muAux = mu[:]
		muAux.sort()
		muestraR.append(muAux)
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


muestra = []
def main(NIND = 1, MAXGE = 2 , NMUESTRA = 80, PROFUNDIDAD = 4 ,indEli =8,PC = 60,PM = 2):
	global muestra
	"""
	NIND = 80
	MAXGE = 200
	NMUESTRA = 80
	PROFUNDIDAD = 5
	indEli = 4
	PC = 60
	PM = 2
	"""
	TiempoTotal = 0
	tiempo_inicial = time()

	MaxGen = []
	muestra = genMuestra(NMUESTRA)
	Pob = PoblacionInicial.aleatorio(NIND,PROFUNDIDAD)
	Calificacion.adaptacion(Pob,muestra[0],muestra[1])
	
	gen = 0

	f.write("{ \"Generacion\" :[" ) # ------------ JSON
	while(gen<MAXGE):

		NuevaPob = []
		print gen
		for i in xrange(0,(NIND-(indEli)/2)/2):
			sel = seleccion.ruleta(Pob)
			ResMez = Mezcla.Punto(sel,PC)
			NuevaPob.append(ResMez[0])
			NuevaPob.append(ResMez[1])


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
		#GenEli = ordenarTam( GenEli )

		#for i in xrange(0,indEli/2):
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
	tiempo_final = time()
	TiempoTotal +=  tiempo_final - tiempo_inicial

	f.write( "], \"TiempoTotal\":\" "+str(TiempoTotal)+" \" }" ) #------------- JSON

	


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

	#-------------------------------------------------------------------------------

	return Pob[ind]


#main(NIND = 100 , MAXGE = 100 , NMUESTRA = 80, PROFUNDIDAD = 4 ,indEli =4,PC = 60,PM = 2)

for inArchivo in xrange(1,2):

	print "Prueba"+str(inArchivo)
	poMax = Individuo.Individuo(5)	
	poMax.error = 80 ## El mejor resultado de todos lo resultados
	PMa = 0 
	TiempoTotal = 0

	iteracion = 1
	for nArchivo in xrange(0,1):
		#f_latex=open("salida_latex.txt","w")
		f=open("2_10.json","w")
		f.write("{ \"Salida\" :[" ) # ------------ JSON
		for x in xrange(0,iteracion):
			f.write("{ \"Prueba\" :[" ) # ------------ JSON

			
			i = main(NIND = 100, MAXGE = 100 , NMUESTRA=50, PROFUNDIDAD = 8  ,indEli=10 ,PC = 60,PM = 90)

			
			if x < iteracion-1: 
				f.write( "]}," )
			else:
				f.write( "]}" )
			print i.gen
			print muestra[0][0]
			print muestra[1][0]
			print poMax.evaluarGen(muestra[0][0])
			print "Error : "+str(i.error) 
			print "Pro Mutacion : " + str(i.calificacion)

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
		print muestra[0][0]
		print muestra[1][0]
		print poMax.evaluarGen(muestra[0][0])
		print "Error : "+str(poMax.error)
		print "Pro Mutacion : " + str(poMax.calificacion)
		print "---------------------------------------"

		#f_latex.close()
f.close()