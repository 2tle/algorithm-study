import sys
input = sys.stdin.readline

Query = input().split('-')
MEM = []
result = 0
for x in Query:
    t = 0
    Sum = x.split('+')
    for y in Sum:
        t = t + int(y)
    MEM.append(t)
result = MEM[0]
for x in range(1,MEM.__len__()):
    result = result - MEM[x]
print(result)