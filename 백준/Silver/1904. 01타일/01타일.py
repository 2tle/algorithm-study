import sys
input = sys.stdin.readline

dp = [0,1,2,3,5]

N = int(input())

for x in range(5,N+1):
    dp.append((dp[x-1] + dp[x-2])%15746)

print(dp[N])