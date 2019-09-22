palabra=input("Introduzca una palabra: ")
palindromo = palabra[::-1]
if palindromo==palabra:
    print("Es un palindromo")
else:
    print("No es un palindromo")