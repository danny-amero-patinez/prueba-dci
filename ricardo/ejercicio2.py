hola = open("archivo.txt", "r")
leer = hola.read()
hola.close()
contador = 0
for x in hola:
	if c == "a":
		contador = contador+1
		print(contador)

print(leer)
