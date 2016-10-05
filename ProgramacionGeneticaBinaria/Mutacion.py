import Individuo
import random
import Mezcla
import PoblacionInicial

def punto (Pob,prof,PM = 2):
	#print "------------ MUTACION ---------"   
	for i in xrange(0,len(Pob)) :
		if random.random()*100 < PM:
			a = PoblacionInicial.aleatorio(1,prof)[0]
			ResMez = Mezcla.Punto([Pob[i],a],100)
			"""
			print "------------Iniciar-----------"
			print Pob[i].gen
			print "            "
			print ResMez[1].gen 
			print "            "
			print a.gen
			print "            "
			print "---------Finalizar------------"
			"""
			Pob[i] = ResMez[0]

