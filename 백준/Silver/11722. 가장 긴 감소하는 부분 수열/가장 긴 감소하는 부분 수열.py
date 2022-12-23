import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
dp = [0]*N
result = 0

for x in range(0,N):
    for y in range(0, N):
        if A[x] < A[y] and dp[x] < dp[y]:
            dp[x] = dp[y]
    dp[x] += 1

print(max(dp))