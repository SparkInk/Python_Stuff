n = int(input('Enter a number up to calculate: '))
L = list()
L1 = list()
for i in range(2, n):
    L.append(i)
for p in L:
	L1.clear()
	for i in L:
		L1.append(p * i)
	for x in L:
		for y in L1:
			if x == y:
				L.remove(x)
print('Prime numbers up to', n, 'is:', L)
