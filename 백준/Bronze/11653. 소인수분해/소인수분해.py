import sys

def soinsu(N):
    t = 2
    while t <= N:
        if N%t==0:
            print(t)
            N = N // t
        else:
            t += 1


X = int(sys.stdin.readline())
soinsu(X)