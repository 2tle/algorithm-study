import sys
input = sys.stdin.readline

N = int(input())

MEET = []
for x in range(N):
    start, end = map(int, input().split())
    MEET.append([start,end])
MEET.sort(key = lambda x: (x[1], x[0] ))

cnt = 0
end = 0
for x,y in MEET:
    if x >= end:
        cnt = cnt + 1
        end = y
print(cnt)