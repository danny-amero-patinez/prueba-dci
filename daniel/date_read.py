s = []
r = []
aa = 0
mm = 0
dd = 0

x = input("DATE 1:\n")
y = x.split("/")

w = input("\nDATE 2:\n")
z = w.split("/")

for i in range(len(y)):
	f = int(y[i], 10)
	s.append(f)
	e = int(z[i], 10)
	r.append(e)

if s[2] >= r[2]:
	aa = s[2] - r[2]
	if s[1] >= r[1]:
		mm = s[1] - r[1]
		if s[0] >= r[0]:
			dd = s[0] - r[0]
		else:
			dd = r[0] - s[0]
	else:
		mm = r[1] - s[1]
		if s[0] >= r[0]:
			dd = s[0] - r[0]
		else:
			dd = r[0] - s[0]
else:
	aa = r[2] - s[2]
	if s[1] >= r[1]:
		mm = s[1] - r[1]
		if s[0] >= r[0]:
			dd = s[0] - r[0]
		else:
			dd = r[0] - s[0]
	else:
		mm = r[1] - s[1]
		if s[0] >= r[0]:
			dd = s[0] - r[0]
		else:
			dd = r[0] - s[0]

print("\nLa diferencia es de "  + str(dd) + " dias, " + str(mm) + " meses, " + str(aa) + " periodos.")
dd = aa*366 + mm*30 + dd
print("\nO lo que seria igual a " + str(dd) + " dias.")

"""for i in range(len(s)-1, -1, -1):
	if s[i] >= r[i]:
		aa ="""