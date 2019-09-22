import time
x = input("Introduzca la frase o palabra: ")
y = [w for w in x if w != " "]
v = 1
y_middle = len(y)//2
s = False

for i in range(0, y_middle):
	if y[i] == y[i-v]:
		print("comprobando..")
		time.sleep(1)
		s = True
	else:
		print("comprobando..")
		time.sleep(1)
		s = False
		break
	v += 2

if s == True:
	print("\nEs un palindromo!")
else:
	print("\nNo lo es.")