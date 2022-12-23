import sys
input = sys.stdin.readline

N = int(input())
P= list(map(int, input().split()))
P.sort()
cnt = 0
for i in range(1,N+1):
    cnt = cnt + sum(P[:i])
print(cnt)