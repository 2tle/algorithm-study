import sys
N = int(sys.stdin.readline())
for x in range(N):
    X,Y = map(int, sys.stdin.readline().split())
    print(X+Y)