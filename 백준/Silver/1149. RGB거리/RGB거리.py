import sys
input = sys.stdin.readline

N= int(input())
rgb =[]

for x in range(N):
    rgb.append(list(map(int, input().split())))

for x in range(1,N):
    rgb[x][0] = min(rgb[x-1][1], rgb[x-1][2]) + rgb[x][0]
    rgb[x][1] = min(rgb[x-1][0], rgb[x-1][2]) + rgb[x][1]
    rgb[x][2] = min(rgb[x-1][0], rgb[x-1][1]) + rgb[x][2]
print(min(rgb[N-1]))