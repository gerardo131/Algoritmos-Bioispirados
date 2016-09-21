import Posfija
class Individuo:
	gen=[]
	prof=0
	calificacion=5
	def __init__(self,prof):
		self.prof=prof
		self.gen=Posfija.crear(prof)

