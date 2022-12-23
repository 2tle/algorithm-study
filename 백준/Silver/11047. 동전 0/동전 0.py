import sys
input = sys.stdin.readline

N,K = map(int, input().split())
A = []
cnt = 0
for _ in range(N):
    t = int(input())
    if t <= K:
        A.append(t)

for x in A[::-1]:
    if x <= K:
        cnt = cnt + (K // x)
        K = K % x
print(cnt)