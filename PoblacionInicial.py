#--------------------- Poblacion inicial ------------------------
def PoInAl(nind, nvar):
	global UMAX
	global UMIN
	global PRECI

	pob=[]
	for i in xrange(0,nind):
		ind =[]
		for j in xrange(0,nvar):
			if len(UMAX)==1:
				fen=codBin(  random.randrange(UMIN[0],UMAX[0]))
			else:
				fen=codBin(  random.randrange(UMIN[j],UMAX[j]))
			ind.append(fen)
		pob.append(ind)
	return pob