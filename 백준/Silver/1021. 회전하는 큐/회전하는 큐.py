import sys
input = sys.stdin.readline

N,M = map(int, input().split())
Query = list(map(int, input().split()))
L = []
c=0
for x in range(1,N+1):
    L.append(x)
for x in range(M):
    length = len(L)
    idx = L.index(Query[x])

    if idx < length - idx:
        while True:
            if Query[x] == L[0]:
                del L[0]
                break
            else:
                L.append(L[0])
                del L[0]
                c= c+1
    else:
        while True:
            if Query[x] == L[0]:
                del L[0]
                break
            else:
                L.insert(0,L[-1])
                del L[-1]
                c = c+1
print(c)

