lista =[]
for i in range(6,312305843008139952128):
	contador = 0
	for x in range(1,(i // 2)+1 ):
		if i % x == 0:

			contador = contador + x

	if contador == i:
		lista.append(i)
		print(lista)





    
