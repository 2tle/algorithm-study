import sys
from collections import deque
input =sys.stdin.readline

N,M = map(int,input().split())
Miro = []
for x in range(N):
    #t = input().strip()
    #t = list(map(int, str(t)))
    t = list(map(int, input().strip()))
    Miro.append(t)

dx = [-1,1,0,0]
dy = [0,0,-1,1]
deq = deque()
deq.append((0,0))

while deq:
    x,y = deq.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx<0 or nx>=N or ny<0 or ny>=M:
            continue
        if Miro[nx][ny] == 0:
            continue
        if Miro[nx][ny] == 1:
            Miro[nx][ny] = Miro[x][y] + 1
            deq.append((nx,ny))
print(Miro[N-1][M-1])