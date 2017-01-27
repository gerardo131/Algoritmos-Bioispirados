#################### NO SOPORTA SOBRE CARGA DE OPERADORES ################################

###############################
#Los Tipos de datos seran 
#--Real  = R
#--Block = MB
#--Bool  =  B
#--Memosi= Me
###############################
import random
numVar = 10
numVarCon = 3
numVarConB = 3

setTyp = ["R","MB","B","MeR"]

setFun = [
			{ "Name" : "+" , "NumPar" : 2, "NumSal" : 1, "TypePar":[ ["R"], ["R"]  ], "Type" : "R"      },
			{ "Name" : "-" , "NumPar" : 2, "NumSal" : 1, "TypePar":[ ["R"], ["R"]  ], "Type" : "R"      },
			{ "Name" : "*" , "NumPar" : 2, "NumSal" : 1, "TypePar":[ ["R"], ["R"]  ], "Type" : "R"      },
			{ "Name" : "/" , "NumPar" : 2, "NumSal" : 1, "TypePar":[ ["R"], ["R"]  ], "Type" : "R"      },

			#{ "Name" : "==", "NumPar" : 2, "NumSal" : 1, "TypePar":[ ["R"], ["R"]  ], "Type" : "B"      },
			#{ "Name" : "!=", "NumPar" : 2, "NumSal" : 1, "TypePar":[ ["R"], ["R"]  ], "Type" : "B"      },
			#{ "Name" : "<=", "NumPar" : 2, "NumSal" : 1, "TypePar":[ ["R"], ["R"]  ], "Type" : "B"      },
			#{ "Name" : ">=", "NumPar" : 2, "NumSal" : 1, "TypePar":[ ["R"], ["R"]  ], "Type" : "B"      },
			#{ "Name" : "<" , "NumPar" : 2, "NumSal" : 1, "TypePar":[ ["R"], ["R"]  ], "Type" : "B"      },
			#{ "Name" : ">" , "NumPar" : 2, "NumSal" : 1, "TypePar":[ ["R"], ["R"]  ], "Type" : "B"      },

			#{ "Name" : "and", "NumPar" : 2, "NumSal" : 1, "TypePar":[ ["B"], ["B"]  ], "Type" : "B"      },
			#{ "Name" : "or" , "NumPar" : 2, "NumSal" : 1, "TypePar":[ ["B"], ["B"]  ], "Type" : "B"      },
			#{ "Name" : "not", "NumPar" : 1, "NumSal" : 1, "TypePar":[ ["B"], ["B"]  ], "Type" : "B"      },

			#{ "Name" : "for"  , "NumPar" : 3, "NumSal" : 1, "TypePar":[ ["R"], ["R"], ["MB"]  ], "Type" : "MB"       },
			#{ "Name" : "while", "NumPar" : 2, "NumSal" : 1, "TypePar":[ ["B"], ["MB"] ]        , "Type" : "MB"       },

			#{ "Name" : "if", "NumPar" : 3, "NumSal" : 1, "TypePar":[ ["B"], ["MB"], ["MB"]  ], "Type" : "MB"      },

			#{ "Name" : "Block2", "NumPar" : 2, "NumSal" : 1, "TypePar":[ ["MB"], ["MB"]  ],                         "Type" : "MB"      },
			#{ "Name" : "Block3", "NumPar" : 3, "NumSal" : 1, "TypePar":[ ["MB"], ["MB"], ["MB"]  ],                 "Type" : "MB"      },
			#{ "Name" : "Block4", "NumPar" : 4, "NumSal" : 1, "TypePar":[ ["MB"], ["MB"], ["MB"], ["MB"]  ],         "Type" : "MB"      },
			#{ "Name" : "Block5", "NumPar" : 5, "NumSal" : 1, "TypePar":[ ["MB"], ["MB"], ["MB"], ["MB"], ["MB"]  ], "Type" : "MB"      },

		#	{ "Name" : "print", "NumPar" : 1, "NumSal" : 1, "TypePar":[ ["R"] ], "Type" : "B"      },
			
		#	{ "Name" : "=B", "NumPar" : 2, "NumSal" : 1, "TypePar":[ ["MeB"]  ], 		"Type" : "B"      },
			{ "Name" : "=R", "NumPar" : 2, "NumSal" : 1, "TypePar":[ ["MeR"], ["R"]  ], "Type" : "MB"       },

		#	{ "Name" : "$B", "NumPar" : 1, "NumSal" : 1, "TypePar":[ ["MeB"]  ], "Type" : "B"      },
			{ "Name" : "$R", "NumPar" : 1, "NumSal" : 1, "TypePar":[ ["MeR"]  ], "Type" : "R"      }

		]
InputVar = [{ "Name" : chr(i) , "Type" :"MeR" } for i in xrange(97,97+numVar) ]
setTer =  InputVar +[ { "Name" : 'Cons'+chr(i) , "Type" :"R" } for i in xrange(97,97+numVarCon) ] + [ { "Name" : 'ConsB'+chr(i) , "Type" :"B" } for i in xrange(97,97+numVarConB) ]  + [{ "Name" : 'None' , "Type" :"MB" }]

valCon  = [random.randint( 0,20 ) for i in xrange(0,numVarCon)]
valConB = [random.choice([True, False]) for i in xrange(0,numVarConB)]

def nameTyp(Set):
	TerTyp={}
	for i in setTyp :
		TerTyp[i]=[]
		for j in Set:
			if j["Type"] == i:
				TerTyp[i].append(j["Name"])
	return TerTyp
def nameFunPar ():
	FunPar ={}
	for i in setFun:
		FunPar[i["Name"]]= {"NumPar":i["NumPar"],"TypePar":i["TypePar"] }
	return FunPar

TerAndTy = nameTyp(setTer)
FunAndTy = nameTyp(setFun)
Funcion  = [i["Name"] for i in setFun]
Terminal = [i["Name"] for i in setTer]
FunPar = nameFunPar()
  
#print  FunPar
#print Funcion
#print Terminal
#print TerAndTy
#print FunAndTy



