import sys
input = sys.stdin.readline

N,C = map(int, input().split())

Cx, Cy = N,N

for x in range(C):
    Y,X = map(int, input().split())
    if Cy <= Y or Cx <= X or X == 0 or Y == 0:
        continue
    
    if Cy * X <= Cx * Y:
        Cy = Y
    else:
        Cx = X
print("%d" %(Cx * Cy))