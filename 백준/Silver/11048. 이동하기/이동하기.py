import sys
input = sys.stdin.readline
N,M = map(int, input().split())

miro = [[0] * (M+1)] * (N+1)

candy = []
for x in range(N):
    candy.append(list(map(int, input().split())))

for x in range(1,N+1):
    for y in range(1,M+1):
        miro[x][y] = max(miro[x-1][y], miro[x][y-1], miro[x-1][y-1]) + candy[x-1][y-1]

print(miro[N][M])