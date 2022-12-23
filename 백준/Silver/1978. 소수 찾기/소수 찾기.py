import sys

N = int(sys.stdin.readline())
M = list(map(int, sys.stdin.readline().split()))
C = 0
for i in M:
    if i == 1:
        continue
    count = 0
    for k in range(2,i+1):
        if i%k==0:
            count += 1
    if(count == 1):
        C += 1
print(C)