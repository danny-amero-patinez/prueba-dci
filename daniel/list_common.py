l1 = []
l2 = []
l3 = []

x = int(input("Primera lista: "))
for i in range(x):
	j = int(input())
	l1.append(j)

print("")

y = int(input("Segunda lista: "))
for i in range(y):
	j = int(input())
	l2.append(j)	

for i in range(x):
	for j in range(y):
		if l1[i] == l2[j]:
			l3.append(l1[i])

print(l3)