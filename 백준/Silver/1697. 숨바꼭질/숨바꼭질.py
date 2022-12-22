import sys
from collections import deque
input = sys.stdin.readline

def func(N,K):
    deq = deque([N])
    distance = [0] * (10**5 + 1)
    while deq:
        temp = deq.popleft()
        if temp == K:
            return distance[temp]
        for x in (temp-1, temp+1, 2* temp):
            if 0<=x<=(10**5) and not distance[x]:
                distance[x] = distance[temp] + 1
                deq.append(x)


N,K = map(int, input().split())
print(func(N,K))