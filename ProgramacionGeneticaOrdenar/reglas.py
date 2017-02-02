#################### NO SOPORTA SOBRE CARGA DE OPERADORES ################################

###############################
#Los Tipos de datos seran 
#--Real  = R
#--Block = MB
#--Bool  =  B
#--Memosi= Me
#--SET
###############################
import random
numInPutVar = 10
numFreeVar  = 2
numVar = numInPutVar + numFreeVar
numVarCon = 3
numVarConB = 3
numDinVar=100

setTyp = ["R","MB","B","MeR","SET"]
setFun = [
			{ "Name" : "+" , "NumPar" : 2, "NumSal" : 1, "TypePar":[ ["R","MeR"], ["R","MeR"]  ], "Type" : ["R"]      },
			{ "Name" : "-" , "NumPar" : 2, "NumSal" : 1, "TypePar":[ ["R","MeR"], ["R","MeR"]  ], "Type" : ["R"]      },
			{ "Name" : "*" , "NumPar" : 2, "NumSal" : 1, "TypePar":[ ["R","MeR"], ["R","MeR"]  ], "Type" : ["R"]      },
			{ "Name" : "/" , "NumPar" : 2, "NumSal" : 1, "TypePar":[ ["R","MeR"], ["R","MeR"]  ], "Type" : ["R"]      },

			{ "Name" : "==", "NumPar" : 2, "NumSal" : 1, "TypePar":[ ["R","MeR"], ["R","MeR"]  ], "Type" : ["B"]      },
			{ "Name" : "!=", "NumPar" : 2, "NumSal" : 1, "TypePar":[ ["R","MeR"], ["R","MeR"]  ], "Type" : ["B"]      },
			{ "Name" : "<=", "NumPar" : 2, "NumSal" : 1, "TypePar":[ ["R","MeR"], ["R","MeR"]  ], "Type" : ["B"]      },
			{ "Name" : ">=", "NumPar" : 2, "NumSal" : 1, "TypePar":[ ["R","MeR"], ["R","MeR"]  ], "Type" : ["B"]      },
			{ "Name" : "<" , "NumPar" : 2, "NumSal" : 1, "TypePar":[ ["R","MeR"], ["R","MeR"]  ], "Type" : ["B"]      },
			{ "Name" : ">" , "NumPar" : 2, "NumSal" : 1, "TypePar":[ ["R","MeR"], ["R","MeR"]  ], "Type" : ["B"]      },

			{ "Name" : "and", "NumPar" : 2, "NumSal" : 1, "TypePar":[ ["B"], ["B"]  ], "Type" : ["B"]      },
			{ "Name" : "or" , "NumPar" : 2, "NumSal" : 1, "TypePar":[ ["B"], ["B"]  ], "Type" : ["B"]      },
			{ "Name" : "not", "NumPar" : 1, "NumSal" : 1, "TypePar":[ ["B"], ["B"]  ], "Type" : ["B"]      },

			{ "Name" : "for"  , "NumPar" : 3, "NumSal" : 1, "TypePar":[ ["SET"], ["R","MeR"], ["MB"]  ], "Type" : ["MB"]       },
			{ "Name" : "while", "NumPar" : 2, "NumSal" : 1, "TypePar":[ ["B"], ["MB"] ]        , "Type" : ["MB"]       },

			{ "Name" : "if", "NumPar" : 3, "NumSal" : 1, "TypePar":[ ["B"], ["MB"], ["MB"]  ], "Type" : ["MB"]      },

			{ "Name" : "Block2", "NumPar" : 2, "NumSal" : 1, "TypePar":[ ["MB"], ["MB"]  ],                         "Type" : ["MB"]      },
			{ "Name" : "Block3", "NumPar" : 3, "NumSal" : 1, "TypePar":[ ["MB"], ["MB"], ["MB"]  ],                 "Type" : ["MB"]      },
			{ "Name" : "Block4", "NumPar" : 4, "NumSal" : 1, "TypePar":[ ["MB"], ["MB"], ["MB"], ["MB"]  ],         "Type" : ["MB"]      },
			{ "Name" : "Block5", "NumPar" : 5, "NumSal" : 1, "TypePar":[ ["MB"], ["MB"], ["MB"], ["MB"], ["MB"]  ], "Type" : ["MB"]      },

		#	{ "Name" : "print", "NumPar" : 1, "NumSal" : 1, "TypePar":[ ["R"] ], "Type" : ["B"]      },
			
		#	{ "Name" : "=B", "NumPar" : 2, "NumSal" : 1, "TypePar":[ ["MeB"]  ], 		"Type" : ["B"]      },
			{ "Name" : "=R", "NumPar" : 2, "NumSal" : 1, "TypePar": [ ["MeR"], ["R"]  ], "Type" : ["MB"]       },
			{ "Name" : "set-", "NumPar" : 1, "NumSal" : 1, "TypePar":[  ["R"]  ], "Type" : ["SET"]     },

		#	{ "Name" : "$B", "NumPar" : 1, "NumSal" : 1, "TypePar":[ ["MeB"]  ], "Type" : ["B"]      },
		#	{ "Name" : "$R", "NumPar" : 1, "NumSal" : 1, "TypePar":[ ["MeR"]  ], "Type" : ["R"]  }

		]
InputVar = [{ "Name" : "IPV_"+str(i) , "Type" :["MeR"] } for i in xrange(0,numInPutVar) ]
FreeVar = [{ "Name" : "FV"+chr(i) , "Type" :["MeR"] } for i in xrange(97,97+numFreeVar) ]
DinVar = [{ "Name" : "DinV_"+str(i) , "Type" :["R"] } for i in xrange(0,numDinVar)]

Cons= [ { "Name" : 'Cons'+chr(i) , "Type" :["R"], "Val":random.randint( 0,20 ) } for i in xrange(97,97+numVarCon) ]+[ { "Name" : 'ConsB'+chr(i) , "Type" :["B"], "Val": random.choice([True, False]) } for i in xrange(97,97+numVarConB) ]+ [{ "Name" : 'None' , "Type" :["MB"],"Val":"pass" }] 
setTer =  InputVar+ FreeVar+ Cons 

def nameTyp(Set):
	TerTyp={}
	for i in setTyp :
		TerTyp[i]=[]
		for j in Set:
			if i in j["Type"]:
				TerTyp[i].append(j["Name"])
	return TerTyp
def nameFunPar ():
	FunPar ={}
	for i in setFun:
		FunPar[i["Name"]]= {"NumPar":i["NumPar"],"TypePar":i["TypePar"] }
	return FunPar
def ConsVal ():
	consval={}
	for i in Cons:
		consval[i["Name"]]=i["Val"]
	return consval	
#Son arreglos que contienen los tipos de datos y el nombre de la funciones 
TerAndTy = nameTyp(setTer)
FunAndTy = nameTyp(setFun)
DinVartry = nameTyp(DinVar)

# Son arreglos que contiene todos los nombres de las funciones
Funcion  = [i["Name"] for i in setFun]
Terminal = [i["Name"] for i in setTer]
DinamicVar = [i["Name"] for i in DinVar] 
NameInputVar = [i["Name"] for i in InputVar]
NameFreevar  = [i["Name"] for i in FreeVar]
NameVar      = NameFreevar + NameInputVar + DinamicVar
NameCons     = [i["Name"] for i in Cons]

#Son arreglos con el nombre de las constantes y el valor 
ValCons      = ConsVal()

#Contiene  el nombre y el numero de parametros y el tipo de cada parametro
FunPar = nameFunPar()

#print  FunPar
#print Funcion
#print Terminal
#print TerAndTy
#print FunAndTy


 

