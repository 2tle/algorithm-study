import sys
L = [0 for i in range(42)]

for _  in range(10):
    N = int(sys.stdin.readline())
    L[N%42] = L[N%42] + 1

c = 0
for x in L:
    if x != 0:
        c = c+ 1

print(c)