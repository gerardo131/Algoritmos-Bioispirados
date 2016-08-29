# funcion de adaptacion 
def adap(X,fmax,fmin):
	return fmax + fmin - fobj(X)

#busqueda de genotipo con valor de funcion objetivo maximo y minimo
def adapMaxMin(pob):
	aux =[]
	sumAux =0
	for i in xrange(0,len(pob)):
		aux.append(fobj(pob[i]))
		sumAux+=aux[i]
	return max(aux),min(aux),(sumAux/len(pob))

# buscar maximo y minimo de la funcion escalada
def MaxMin(pob,a,b):
	aux =[]
	for i in xrange(0,len(pob)):
		aux.append(escalado(fobj(pob[i]),a,b))
	return max(aux),min(aux)

#Encontrar los coeficientes de de la funcion escalada 
def preEscalar(umax,umin,uprom):
	fmultiple = 1.2
	delta = 0.0
	a=0.0
	b=0.0
	if umin >(fmultiple*uprom - umax)/(fmultiple-1.0): # prueba de no negatividad 
		# scala normal
		delta = umax- uprom+0.00001

		a=(fmultiple-1.0)*uprom/delta
		b=uprom*(umax - fmultiple*uprom)/delta
	else:
		delta = uprom- umin +0.00001
		a=uprom /delta
		b=-umin* uprom/ delta
	return a,b

#crear la funcion escalada
def escalado(f,a,b,):
	return a*f+b

#-------------------- Calificacion ----------------------------- 

def cal(pob): 
	val=[]
	aco=0
	fmax,fmin,pp = adapMaxMin(pob)
	a,b=preEscalar(fmax,fmin,pp)
	Emax,Emin = MaxMin(pob,a,b)


	
	for i in xrange(0,len(pob)):
		aco+=float( -escalado(fobj(pob[i]),a,b) +Emax+Emin )

	for i in xrange(0,len(pob) ):
		if aco ==0 :
			val.append(0.0)
		else:
			val.append( float( -escalado(fobj(pob[i]),a,b) +Emax+Emin )/float(aco) )
	return val	
	
#-------------------------- Mezclar ------------------------------
