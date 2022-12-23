import sys

R = int(sys.stdin.readline())
for _ in range(R):
    p = 1
    pp = 0
    L = sys.stdin.readline()
    for x in L:
        if x == 'O':
            pp = pp + p
            p = p + 1
        else:
            p = 1
    print(pp)