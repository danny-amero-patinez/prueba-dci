l = open("PruebaTexto.txt", "r")
palabras = 0
word_change = False
caracteres = 0
s = []


for line in l.readlines():
	for c in line:
		#s.append(j)
		if word_change == True:
			if c == ' ' or c == "\n" or c == "\t":
				palabras += 1
				word_change = False
		if c != ' ' or c != "\n" or c != "\t":
			word_change = True
		caracteres += 1

#En caso de que solo exista una palabra y al principio del texto
"""if palabras == 0:
	for i in s:
		if i != '' or i != "\n" or i != "\t":
			palabras += 1"""

print("El total de palabras es: " + str(palabras))
print("El total de caracteres es: " + str(caracteres))