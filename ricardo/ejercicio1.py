lista = [1,2,3,4,5,6,7,8,9,10]
lista2 =[]
contador = 0
contador2 = 0
while contador <= 10:
	contador = contador+1
	print("dame un numero")
	numero = int(input("aqui: "))
	lista2.append(numero)
	if contador == 10:
		print(lista)
		print(lista2)
		break;
for x in lista:
	for y in lista2:
		if x==y:
			contador2 = contador2+1
print("son",contador2,"numeros en comun")
