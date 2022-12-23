import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
Ar = A[::-1]
#Ar.reverse()

dp1 = [1]*N
dp2 = [1]*N
r = []

for x in range(N):
    for y in range(x):
        if A[x] > A[y]:
            dp1[x] = max(dp1[x] , dp1[y] + 1)
        if Ar[x] > Ar[y]:
            dp2[x] = max(dp2[x] , dp2[y] + 1)
for x in range(N):
    r.append(dp1[x] + dp2[N-x-1]-1)
print(max(r)) 