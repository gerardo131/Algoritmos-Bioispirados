import Individuo
import thread

################### funcion de adaptacion ############################3
terminoHilo = 0
emp = 0
def getError (i,valE,resE):
	global terminoHilo
	i.EMC(valE,resE)
	terminoHilo+=1

	#print i.gen
	print "adios " + str(terminoHilo) 
def adaptacion(pob,valE,resE):
	global terminoHilo
	terminoHilo = 0
	Aerror = []
	N=0
	for i in pob:
	#	print i.gen
	#	print "hola"
		#getError (i,valE,resE)
		thread.start_new_thread(getError,(i,valE,resE))
		N+=1
		print "###################-- "+str(N)
		print i.gen
		print "####################"
	#print "calificando"
	#print terminoHilo
	#print terminoHilo == len(pob)
	while (terminoHilo != len(pob)):
		pass
	#print "###############termino de calificar#########################"

	for i in xrange( 0,len(pob) ):
		pob[i].calificacion = 1000000.0- pob[i].error
