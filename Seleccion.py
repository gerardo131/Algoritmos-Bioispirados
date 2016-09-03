import math
from operator import xor
import random
import numpy as np

def ruleta(cal,pob):
	sumCal = 0
	
	res = [0,0]
	for j in xrange(0,2):
		calAcom=0
		for k in xrange(0,len(cal)):
			sumCal += cal[k]
		r = random.random()
		rand = r*sumCal
		i=0
		while(i<len(cal) and calAcom<rand ):
			calAcom += cal[i]
			i+=1
		if i!=0 :
			res[j]=i-1
	return res