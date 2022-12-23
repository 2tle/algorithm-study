import sys
input = sys.stdin.readline

N,M = map(int, input().split())
Height = list(map(int, input().split()))

sorted(Height)

start = 0
end = 2000000000
juldan = 0

def func():
    s=0
    for x in Height:
        if x > mid:
            s = s + (x - mid)
    return s

while start<=end:
    mid = (start + end) // 2
    if (func()) >= M:
        juldan = mid
        start = mid + 1
    else:
        end = mid - 1
print(juldan)
