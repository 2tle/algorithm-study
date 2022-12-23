import sys

input = sys.stdin.readline

N,M = map(int, input().split())
Mbyte = [0] + list(map(int, input().split()))
C = [0] + list(map(int, input().split()))

dp = [[0 for _ in range( sum(C) + 1 )] for _ in range(N + 1)]

cur = 100 * 100 + 1

for x in range(1, N+1):
    mem = Mbyte[x]
    biyong = C[x]

    for y in range(1, sum(C) + 1):
        dp[x][y] = dp[x-1][y]
    
    for y in range(biyong, sum(C) + 1):
        dp[x][y] = max(dp[x][y], dp[x-1][y-biyong] + mem)

        if dp[x][y] >= M:
            cur = min(cur, y)

print(cur)