import validacion
import crypto

while True:
	opcion=input("\nBienvenido esta en el proyecto de Programación (0790) parte 1.\n1.validar entero.\n2.validar float.\n3.validar complex.\n4.validar lista.\n5.comprobar encriptado.\n6.cerrar.\nseleccione que desea comprobar: ")
	#validación de los integer
	if opcion=="1":
		try:
			print(validacion.valInt(4))
			print(validacion.valInt(4.0))
			print(validacion.valInt(4,(4,10)))
			print(validacion.valInt(4,[3,10]))
			print(validacion.valInt(4,[4,10]))
			print(validacion.valInt(4,[10,4]))
			print(validacion.valInt(4,5))
		except:
			print("error.")
	#validación de los tipo float
	elif opcion=="2":
		try:
			print(validacion.valFloat(4.0))
			print(validacion.valFloat(4))
			print(validacion.valFloat(4.4,(4.4,10.0)))
			print(validacion.valFloat(4.4,(4,10)))
			print(validacion.valFloat(4.1,[4.1,9.05]))
			print(validacion.valFloat(4.2,[4,10]))
			print(validacion.valFloat(4.2,[10,4]))
			print(validacion.valInt(4,5))
		except:
			print("error")
	#validación de los tipo complex  
	elif opcion=="3":
		try:
			print(validacion.valComplex(3+4j))
			print(validacion.valComplex(4.0))
			print(validacion.valComplex(3+4j,(5,10)))
			print(validacion.valComplex(3+4j,[5,10]))
			print(validacion.valComplex(3+4j,[4,10]))
			print(validacion.valComplex(3+4j,[10,4]))
			print(validacion.valComplex(3+4j,5))
		except:
			print("error")
	#validación de las listas
	elif opcion=="4":
		try:
			print(validacion.valList([]))
			print(validacion.valList([1,2,3,4,5,6]))
			print(validacion.valList((1)))
			print(validacion.valList(([1,2,3],1,"value")))
			print(validacion.valList([[1,2,3],1,"value"]))
			print(validacion.valList([[1,2,3],123,[3,2,1]]))
			print(validacion.valList([[1,2,3],1,"list"]))
			print(validacion.valList(([1,2,3],1,"list")))
			print(validacion.valList([[1,2,3],[2,6]],"long"))
			print(validacion.valList([1,2,3],1,"long"))
		except:
			print("error")
	#cifrado en binario separados por "-"
	elif opcion=="5":
		print(crypto.encriptador("Hola mundo!"))
		print(crypto.descriptador("0100010-0001111-0001011-0000000-1000000-0001100-0010101-0001101-0000011-0001111-1001000"))
	elif opcion=="6":
		break