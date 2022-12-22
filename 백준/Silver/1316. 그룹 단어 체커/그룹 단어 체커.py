import sys

N = int(sys.stdin.readline())
C = 0
for _ in range(N):
    word = sys.stdin.readline().rstrip()
    L = []
    isGroup = True
    for x in word:
        if ord(x) not in L:
            L.append(ord(x))
        elif ord(x) in L:
            if L[-1] != ord(x):
                isGroup = False
                break
    if isGroup == True:
        C = C + 1
print(C)