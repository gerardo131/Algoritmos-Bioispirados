#################### NO SOPORTA SOBRE CARGA DE OPERADORES ################################

###############################
#Los tipos de datos seran 
#--Real  = R
#--Block = MB
#--Bool  =  B
#--Memosi= Me
###############################
numVar = 10
numVarCon = 3
numVarConB = 3

setFun = [
			{ "Nom" : "+" , "NumPar" : 2, "NumSal" : 1, "TipoPar":[ ["R"], ["R"]  ], "Tipo" :[ ["R"] ]       }
			{ "Nom" : "-" , "NumPar" : 2, "NumSal" : 1, "TipoPar":[ ["R"], ["R"]  ], "Tipo" :[ ["R"] ]       }
			{ "Nom" : "*" , "NumPar" : 2, "NumSal" : 1, "TipoPar":[ ["R"], ["R"]  ], "Tipo" :[ ["R"] ]       }
			{ "Nom" : "/" , "NumPar" : 2, "NumSal" : 1, "TipoPar":[ ["R"], ["R"]  ], "Tipo" :[ ["R"] ]       }

			{ "Nom" : "==", "NumPar" : 2, "NumSal" : 1, "TipoPar":[ ["R"], ["R"]  ], "Tipo" :[ ["B"] ]       }
			{ "Nom" : "!=", "NumPar" : 2, "NumSal" : 1, "TipoPar":[ ["R"], ["R"]  ], "Tipo" :[ ["B"] ]       }
			{ "Nom" : "<=", "NumPar" : 2, "NumSal" : 1, "TipoPar":[ ["R"], ["R"]  ], "Tipo" :[ ["B"] ]       }
			{ "Nom" : ">=", "NumPar" : 2, "NumSal" : 1, "TipoPar":[ ["R"], ["R"]  ], "Tipo" :[ ["B"] ]       }
			{ "Nom" : "<" , "NumPar" : 2, "NumSal" : 1, "TipoPar":[ ["R"], ["R"]  ], "Tipo" :[ ["B"] ]       }
			{ "Nom" : ">" , "NumPar" : 2, "NumSal" : 1, "TipoPar":[ ["R"], ["R"]  ], "Tipo" :[ ["B"] ]       }

			{ "Nom" : "and", "NumPar" : 2, "NumSal" : 1, "TipoPar":[ ["B"], ["B"]  ], "Tipo" :[ ["B"] ]       }
			{ "Nom" : "or" , "NumPar" : 2, "NumSal" : 1, "TipoPar":[ ["B"], ["B"]  ], "Tipo" :[ ["B"] ]       }
			{ "Nom" : "not", "NumPar" : 1, "NumSal" : 1, "TipoPar":[ ["B"], ["B"]  ], "Tipo" :[ ["B"] ]       }

			{ "Nom" : "for"  , "NumPar" : 3, "NumSal" : 1, "TipoPar":[ ["R"], ["R"], ["MB"]  ], "Tipo" :[ ["MB"] ]       }
			{ "Nom" : "while", "NumPar" : 2, "NumSal" : 1, "TipoPar":[ ["B"], ["MB"] ]        , "Tipo" :[ ["MB"] ]       }

			{ "Nom" : "if", "NumPar" : 3, "NumSal" : 1, "TipoPar":[ ["B"], ["MB"], ["MB"]  ], "Tipo" :[ ["B"] ]       }

			{ "Nom" : "and", "NumPar" : 2, "NumSal" : 1, "TipoPar":[ ["MB"], ["MB"]  ],                         "Tipo" :[ ["B"] ]       }
			{ "Nom" : "and", "NumPar" : 3, "NumSal" : 1, "TipoPar":[ ["MB"], ["MB"], ["MB"]  ],                 "Tipo" :[ ["B"] ]       }
			{ "Nom" : "and", "NumPar" : 4, "NumSal" : 1, "TipoPar":[ ["MB"], ["MB"], ["MB"], ["MB"]  ],         "Tipo" :[ ["B"] ]       }
			{ "Nom" : "and", "NumPar" : 5, "NumSal" : 1, "TipoPar":[ ["MB"], ["MB"], ["MB"], ["MB"], ["MB"]  ], "Tipo" :[ ["B"] ]       }

		#	{ "Nom" : "print", "NumPar" : 1, "NumSal" : 1, "TipoPar":[ ["R"] ], "Tipo" :[ ["B"] ]       }
			
		#	{ "Nom" : "=B", "NumPar" : 5, "NumSal" : 1, "TipoPar":[ ["MeB"]  ], "Tipo" :[ ["B"] ]       }
			{ "Nom" : "=R", "NumPar" : 5, "NumSal" : 1, "TipoPar":[ ["MeR"], ["R"]  ], "Tipo" :[ ["MB"] ]       }

		#	{ "Nom" : "$B", "NumPar" : 5, "NumSal" : 1, "TipoPar":[ ["MeB"]  ], "Tipo" :[ ["B"] ]       }
			{ "Nom" : "$R", "NumPar" : 5, "NumSal" : 1, "TipoPar":[ ["MeR"]  ], "Tipo" :[ ["R"] ]       }

		]

setTer = [ { "Nom" : chr(i) , "Tipo" :[ ["MeR"] ] } for i in xrange(97,97+numVar) ]
			+ [ { "Nom" : 'Cons'+chr(i) , "Tipo" :[ ["R"] ] } for i in xrange(97,97+numVarCon) ]
				+ [ { "Nom" : 'ConsB'+chr(i) , "Tipo" :[ ["B"] ] } for i in xrange(97,97+numVarConB) ]

valCon  = [random.randint( 0,20 ) for i in xrange(0,numVarCon)]
valConB = [random.choice([True, False]) for i in xrange(0,numVarConB)]

