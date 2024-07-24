def tamano(valor):
	if(len(valor)>2):
		raise TypeError("Se a ingresado mas de 2 argumentos.")
	if(valor==()):
		raise TypeError("Debe ingresar por lo menos 1 argumento.")

def intervalo(valor):
	if(type(valor)!=list and type(valor)!=tuple):
		raise TypeError("El segundo argumento debe ser un intervalo de tipo list o tuple.")
	if(len(valor)>2 or len(valor)<2):
		raise TypeError("El segundo argumento debe de tener solo 2 valores.")
	if((type(valor[0])!=int or type(valor[1])!=int) and (type(valor[0])!=float or type(valor[1])!=float)):
		raise TypeError("El intervalo debe de ser numeros.")
	if(valor[0] > valor[1]):
		raise ValueError("Este intervalo no existe.")

def valInt(*valor):
	tamano(valor)
	if(len(valor) == 2):
		intervalo(valor[1])
		if(type(valor[0])!=int):
			return(False)
		if(type(valor[1])==list and (valor[0]<valor[1][0] or valor[0]>valor[1][1])):
			return(False)
		if(type(valor[1])==tuple and (valor[0]<=valor[1][0] or valor[0]>=valor[1][1])):
			return(False)
	if(type(valor[0])!=int):
		return(False)
	return(True)

def valFloat(*valor):
	tamano(valor)
	if(len(valor) == 2):
		intervalo(valor[1])
		if(type(valor[0])!=float):
			return(False)
		if(type(valor[1])==list and (valor[0]<valor[1][0] or valor[0]>valor[1][1])):
			return(False)
		if(type(valor[1])==tuple and (valor[0]<=valor[1][0] or valor[0]>=valor[1][1])):
			return(False)
	if(type(valor[0])!=float):
		return(False)
	return(True)

def valComplex(*valor):
	tamano(valor)
	if(len(valor) == 2):
		intervalo(valor[1])
		if(type(valor[0])!=complex):
			return(False)
		if(type(valor[1])==list and (abs(valor[0])<valor[1][0] or abs(valor[0])>valor[1][1])):
			return(False)
		if(type(valor[1])==tuple and (abs(valor[0])<=valor[1][0] or abs(valor[0])>=valor[1][1])):
			return(False)
	if(type(valor[0])!=complex):
		return(False)
	return(True)

def valList(*valor):
	if(len(valor)!=1 and len(valor)!=3):
		raise TypeError("Debe ingresar 1 o 3 argumentos.")
	if(len(valor)==1 and type(valor[0])==list):
		return(True)
	if(len(valor)==3):
		if(type(valor[1])!=list or type(valor[1])!=int):
			raise TypeError("El segundo argumento debe ser una list o un int.")
		if(type(valor[2])!=str):
			raise TypeError("El tercero argumento debe ser un str.")
		if(valor[2].lower()!="value" and valor[2].lower()!="len"):
			raise ValueError("Esto no es un argumento valido.")
		if(valor[2].lower()=="value" and type(valor[0])==list and type(valor[1])==list and valor[0]==valor[1]):
			return(True)
		if(valor[2].lower()=="len" and type(valor[0])==list and len(valor[0])==valor[1]):
			return(True)
	return(False)