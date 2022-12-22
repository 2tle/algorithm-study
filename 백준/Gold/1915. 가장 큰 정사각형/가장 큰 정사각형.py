import sys
input = sys.stdin.readline

N,M = map(int, input().split())

arr = []
for x in range(N):
    arr.append(list(map(int, list(input().strip()))))

dp  = [[0 for col in range(M+1)] for row in range(N+1)]
response = 0

for x in range(1,N+1):
    for y in range(1,M+1):
        if arr[x-1][y-1] == 1:
            #dp[x][y] = min(dp[x-1][y], dp[x][y-1], dp[x-1][y-1]) + 1
            dp[x][y] = min(dp[x][y - 1], min(dp[x - 1][y - 1], dp[x - 1][y])) + 1
        else:
            dp[x][y] = 0
        response = max(response, dp[x][y])

print(response*response)