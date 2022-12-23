import sys
N,X = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
for x in A:
    if x < X:
        print(str(x)+" ", end="")