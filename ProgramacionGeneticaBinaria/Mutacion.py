import Individuo
import random
import Mezcla
import PoblacionInicial
PM = .2

def punto (Pob,prof):
	for i in xrange(0,len(Pob)) :
		if random.random()*10 < PM:
			a = PoblacionInicial.aleatorio(1,prof)[0]
			ResMez = Mezcla.Punto([Pob[i],a])
			Pob[i] = ResMez[0]

