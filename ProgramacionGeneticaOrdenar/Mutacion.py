import Individuo
import random
import Mezcla
import PoblacionInicial

def punto (Pob,prof,PM = 2):
	#print "------------ MUTACION ---------"   
	for i in xrange(0,len(Pob)) :
		if random.random()*100 < PM:
			a = PoblacionInicial.aleatorio(1,random.randint(1,prof) )[0]
			ResMez = Mezcla.Punto([Pob[i],a],100)[0]
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
			Pob[i].gen= ResMez.gen
"""
pru1 = Individuo.Individuo(2)
pru2 = Individuo.Individuo(2)
print pru1.gen 
#contar ( pru1.gen, 5)
print pru2.gen
res = punto([pru1],3,100)
print pru1.gen
"""