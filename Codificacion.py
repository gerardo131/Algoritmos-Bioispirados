def codBin(num):
	Inter=Umax-Umin
	binNum=""
	Bin=""

	binNum=bin(int( ( float(num-Umin)*(2**(preci)-1.0 ) )/(Inter) ) )[2:]
	print int( ( float(num-Umin)*(2**(preci+1.0)-1.0 ) )/(Inter) ) 

	for i in xrange(0,preci-len(binNum)):
		Bin+="0"
	Bin += binNum
	return list(Bin)
	
def dCodBin(Bin):
	Inter =Umax-Umin
	bi=int(''.join(Bin),2)
	num =( (float(bi)* float(Inter))/float(2**(preci)-1.0)+Umin  )
	return num 

	