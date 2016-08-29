def aleatorio(nind, nvar):
	pob=[]
	for i in xrange(0,nind):
		ind =[]
		for j in xrange(0,nvar):
			fen=codBin(  random.randrange(Umin,Umax))
			ind.append(fen)
		pob.append(ind)
	return pob