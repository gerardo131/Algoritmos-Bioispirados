import Codificacion 


	#------------ funcion cuadratica --------------- 
def Cuadratica(x):
	res=0
	res= -1*(dCodBin(x[0])-3)**2 + 100
	return res


	#------------ funcion Ackley -----------------
def Ackley(X):
	var=[]
	for i in xrange(0,len(X)):
		var.append( float(dCodBin(X[i])) )
	
	res=0
	preres = -np.exp(0.5*(np.cos(2.0*np.pi*var[0])+np.cos(2.0*np.pi*var[1]) ) )+np.exp(1)+20.0
	res = -20.0*np.exp( -0.2*np.sqrt(0.5*(var[0]**2+var[1]**2) ) ) + preres
	return res
	#------------------------------------------------

	#------------ funcion Sphere -----------------
def Sphere(X):
	suma=0
	for i in xrange(0,len(X)):
		suma += float(dCodBin(X[i]))**2
	return suma
	#------------------------------------------------


	#------------ funcion Rosenbrock -----------------
def Rosenbrock(X):
	suma=0
	var=[]
	for i in xrange(0,len(X)):
		var.append( float(dCodBin(X[i])) )

	for i in xrange(0,len(X)-1):
		suma += ( 100.0*(var[i+1]-var[i]**2)**2 + (var[i]-1)**2 )
	return suma
	#------------------------------------------------


	#------------ funcion Beale -----------------
def Beale(X):
	var=[]
	for i in xrange(0,len(X)):
		var.append( float(dCodBin(X[i])) )
	return (1.5-var[0]+var[0]*var[1])**2 + (2.25-var[0]+var[0]*var[1]**2)**2 + (2.625-var[0]+var[0]*var[1]**3)**2
	#------------------------------------------------

	#------------- funcion Cross in trayn --------
def Cross_in_trayn(X):
	var=[]
	for i in xrange(0,len(X)):
		var.append( float(dCodBin(X[i])) )
	return -0.0001*( abs( math.sin(var[0])*math.sin(var[1])*math.exp(abs(100.0-math.sqrt(var[0]**2+var[1]**2)/math.pi ) ) ) +1)**(0.1)
	#---------------------------------------------

