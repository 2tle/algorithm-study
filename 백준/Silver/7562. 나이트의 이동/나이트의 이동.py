import sys
input = sys.stdin.readline

dx=[-2,-1,1,2,2,1,-1,-2]
dy=[1,2,2,1,-1,-2,-2,-1]


t= int(input())
from collections import deque
for _ in range(t):
    l = int(input())
    startx, starty = map(int, input().split())
    endx , endy = map(int, input().split())
    arr = [ [0] * l  for _ in range(0,l)]
    arr[startx][starty] = 1

    queue = deque()
    queue.append((startx, starty))
    while queue:
        x, y = queue.popleft()
        if x == endx and y == endy:
            print(arr[x][y] -1)
            break
        for k in range(0, 8):
            nextx = x + dx[k]
            nexty = y + dy[k]
            if (0 <= nextx < l and 0 <= nexty < l) and arr[nextx][nexty] == 0:
                arr[nextx][nexty] = arr[x][y] + 1
                queue.append((nextx, nexty))