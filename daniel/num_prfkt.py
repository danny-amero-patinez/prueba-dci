from itertools import count

total = 0
x = int(input("Por favor, defina el total de numeros perfectos que necesite: "))

def number_validation(n):
	sum = 0
	for i in range(1, n):
		if n % i == 0:
			sum += i
	return sum == n

for i in count():
	l = number_validation(i)
	if l == True:
		print(i)
		total += 1
	if x == total:
		break

#Tarda un chingo para procesar de 6 numeros en adelante jajaja