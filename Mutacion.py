def inversa (pob):
	for i in xrange(0, len(pob)) :
		if random.random()*10 < .2 :
			print "----mutacion-----"
			for j in xrange(0,len(pob[i])):
				for k in xrange(0,len(pob[i][j])):
					if pob[i][j][k] == "1":
						pob[i][j][k] == "0"
					else:
						pob[i][j][k] == "1"
	return pob

