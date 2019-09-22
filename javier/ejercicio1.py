frace = open("texto.txt", "r")
longitud = len(frace)
contador = 0 
for x in frace.readlines():
	for i in range(0,longitud):
    	if (frace[i].isspace()): 
        	contador = contador + 1
    
total_de_letras=longitud-contador 
print("La frase tiene ",total_de_letras,"letras")
palabra1 =(frace.split())
palabra2 = len(palabra1)
print("la frase tiene ",palabra2,"palabras")

frase = close()