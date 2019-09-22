from itertools import count
l = int(input("Cuantos numeros perfectos quieres: "))
lista = []

def num_perfect(n):
	contador = 0
	for x in range(n-1,0,-1):
		if n%x == 0:
			contador = contador+x
			if x == 1:
				if contador == n:
					lista.append(n)
					
for i in count():
	num_perfect(i)
	if len(lista) == l:
		break
print(lista)
				