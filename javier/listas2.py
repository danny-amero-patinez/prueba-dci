
numero = int(input("lista1 = "))
lista1 = []
lista2 = []
lista3 = []
for i in range(numero):
	lista1.append(int(input()))
	#print("lista1 = ",lista1)
print("\n")
numero2 = int(input("lista2 = "))
for x in range(numero2):
	lista2.append(int(input()))
	#print("lista2 = ",lista2)

for y in lista1:
	if y in lista2:
		lista3.append(y)
print(lista3)

