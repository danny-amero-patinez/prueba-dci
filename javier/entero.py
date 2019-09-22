print("este programa elimina los numeros enteros iguales.")
numero = int(input("ingresa un numero entero: "))
lista = []
for i in range(numero):
	print("ingresa",numero," numeros")
	lista.append(int(input()))
	print("lista sin eliminar numeros iguales = ",lista)
lista2 = list(set(lista))    
print("lista con numeros iguales eliminados = ",lista2)	
