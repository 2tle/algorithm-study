import sys
input = sys.stdin.readline
N = int(input())

ald = {'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,'J':0,'K':0,'L':0,'M':0,'N':0,'O':0,'P':0,'Q':0,'R':0,'S':0,'T':0,'U':0,'V':0,'W':0,'X':0,'Y':0,'Z':0,}
all = [ 0 for _ in range(26) ]
for _ in range(N):
    W = input().strip()
    for x in range(len(W)):
        N = 10 ** ( len(W) - (x+1) )
        ald[W[x]] = ald[W[x]] + N

real = []
K = ald.values()
for x in K:
    if x != 0:
        real.append(x)
real.sort(reverse=True)
result = 0
for x in range(len(real)):
    result = result + ( real[x] * (9-x))
print(result)
