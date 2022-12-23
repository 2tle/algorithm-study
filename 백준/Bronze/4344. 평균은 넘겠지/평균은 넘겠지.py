import sys

C = int(sys.stdin.readline())
for _ in range(C):
    L = list(map(int, sys.stdin.readline().split()))
    N = L.pop(0)
    PG = float(sum(L)) / float(N)
    U = 0
    for x in L:
        if x > PG:
            U = U + 1
    print("{:.3f}%".format((float(U) / float(N) * 100)))