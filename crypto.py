def comprobador(letra,abecedario):
	for comprobar in abecedario:
		if(comprobar==letra):
			return(False)
	return(True)

def encriptador(texto):
	abecedario= "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789 .,;:-+_!¡¿?*/<>$%&=^\'\"\\"
	encriptado=""
	for letra in texto:
		if(comprobador(letra,abecedario)):
			continue
		if(encriptado!=""):
			encriptado+="-"
		numero=abecedario.index(letra)
		volteador=""
		for vuelta in range(7):
			if(numero%2==0):
				numero=numero/2
				volteador+="0"
			else:
				numero=(numero-1)/2
				volteador+="1"
		for inversor in range(6,-1,-1):
			encriptado+=volteador[inversor]
	return(encriptado)

def descriptador(encriptado):
	abecedario="abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789 .,;:-+_!¡¿?*/<>$%&=^\'\"\\"
	texto=""
	contador=0
	while True:
		numero=0
		if(contador>0):
			if(encriptado[contador-1]!="-"):
				raise TypeError("El encriptado no es el correcto, error en la linea del texto "+str(contador-1)+".")
		for buscador in range(7):
			if(encriptado[buscador+contador]!="1" and encriptado[buscador+contador]!="0"):
				raise TypeError("El encriptado no es el correcto, error en la linea del texto "+str(buscador+contador+1)+".")
			if(encriptado[buscador+contador]=="1"):
				numero+=2**(6-buscador)
		if(numero>len(abecedario)):
			raise ValueError("El encriptado que añadio no existe.")
		texto+=abecedario[numero]
		contador+=8
		if(contador>len(encriptado)):
			return(texto)
		if(contador+7>len(encriptado)):
			raise ValueError("El encriptado que añadio no existe.")