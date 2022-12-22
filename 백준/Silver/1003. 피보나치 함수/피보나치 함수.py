import sys
input = sys.stdin.readline
A0 = [1,0,1,1]
A1 = [0,1,1,2]

N = int(input())
for x in range(N):
    T = int(input())
    if len(A0) < T+1:
        for y in range(len(A0), T+1):
            A0.append(A0[y-1]+A0[y-2])
            A1.append(A1[y-1]+A1[y-2])
    print(A0[T],A1[T])

