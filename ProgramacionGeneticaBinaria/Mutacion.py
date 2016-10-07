import Individuo
import random
import Mezcla
import PoblacionInicial

def punto (Pob,prof,PM = 2):
	#print "------------ MUTACION ---------"   
	for i in xrange(0,len(Pob)) :
		if random.random()*100 < PM:
			a = PoblacionInicial.aleatorio(1,random.randint(0,prof-1) )[0]
			ResMez = Mezcla.mezclaPunto(Pob[i].gen,a.gen,[random.randint(0,len(Pob[i].gen)-1),len(a.gen)-1])
			"""
			print "------------Iniciar-----------"
			print Pob[i].gen
			print "            "
			print ResMez 
			print "            "
			print a.gen
			print "            "
			print "---------Finalizar------------"
			"""
			Pob[i].gen = ResMez

