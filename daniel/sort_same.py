def sorty(l):
	for i in range(len(l)):
		for j in range(len(l)-1):
			if l[j] >= l[j+1]:
				c_o(l, j, j+1)

def remove_same(l):
	for i in range(len(l)):
		if l[i] not in b:
			b.append(l[i])
			

def c_o(l, x, y):
	var = l[x]
	l[x] = l[y]
	l[y] = var

n = int(input("You have to put a number: "))
a = [0]*n
b = []

for i in range(n):
	a[i] = int(input())

sorty(a)
remove_same(a)
print(c)