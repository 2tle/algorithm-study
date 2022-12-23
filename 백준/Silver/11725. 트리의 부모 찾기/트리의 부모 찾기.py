import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

Tree = [ [] for _ in range(0,n+1)]
for _ in range(0,n-1):
    j1, j2 = map(int, input().split())
    Tree[j1].append(j2)
    Tree[j2].append(j1)
Q = deque()
Q.append(1)

visited = [False ] * (n+1)
result = {}

while Q.__len__() > 0:
    Parent = Q.popleft()
    for x in Tree[Parent]:
        if visited[x] == False:
            result[x] = Parent
            Q.append(x)
            visited[x] = True


for x in range(2,n+1):
    print(result[x])