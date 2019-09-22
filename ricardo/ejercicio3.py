lista = []
numero = int(input("tu numero de numeros de la lista: "))
contador = 0
while numero > 0:
	contador = contador+1
	numeros = int(input("otro numero: "))
	lista.append(numeros)
	if contador == numero:
		break;
print(lista)
lista2 = []
for z in lista:
	if z not in lista2:
		lista2.append(z)

print(lista2)
def pilines(lista2, x, y):
	var_auxiliar = lista2[x]
	lista2[x] = lista2[y]
	lista2[y] = var_auxiliar

def bubble_sort(lista2):
	for x in range(len(lista2)):
		for y in range(len(lista2)-1):
			if lista2[y] <= lista2[y+1]:
				pilines(lista2, y, y+1)
				
bubble_sort(lista2) 
print(lista2)

