N= []
for _ in range(0,9):
	N.append(int(input()))
max=0
maxIdx=0
for x in range(0,9):
	if N[x] > max:
		max=N[x]
		maxIdx = x
print(max)
print(maxIdx+1)