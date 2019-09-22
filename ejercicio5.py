#Hacer un programa que lea dos listas de diferentes tamaños y que genere e imprima una lista con los elementos en común

num1 = int(input("cuantos numeros quieres en tu primera lista: "))
contador1 = 0
lista = []
while contador1 >= 0:
	contador1 = contador1+1
	num_list = int(input("aqui: "))
	lista.append(num_list)
	if contador1 == num1:
		break	
print(lista)

num2 = int(input("cuantos numeros quieres en tu segunda lista: "))
contador2 = 0
lista2 = []
while contador2 >= 0:
	contador2 = contador2+1
	num_list2 = int(input("aqui: "))
	lista2.append(num_list2)
	if contador2 == num2:
		break	
print(lista2)
lista3 = []
for z in lista:
	for y in lista2:
		if z == y:
			print(z)
			lista3.append(z)
print(lista3)

		