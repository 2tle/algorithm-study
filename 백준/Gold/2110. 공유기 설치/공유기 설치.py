import sys
input = sys.stdin.readline

N,C = map(int, input().split())
Xi = []
for x in range(N):
    Xi.append(int(input()))

Xi = sorted(Xi)
start = 0
end = 1000000000
res = 0

def f(x):
    cnt = 1
    beforeX = Xi[0]
    for i in range(1,N):
        if (Xi[i] - beforeX) >= x:
            cnt = cnt + 1
            beforeX = Xi[i]
    return cnt >= C

while start<=end:
    mid = (start + end) // 2
    if f(mid):
        res = mid
        start = mid + 1
    else:
        end = mid - 1
print(res)


