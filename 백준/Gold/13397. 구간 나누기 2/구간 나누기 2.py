import sys
input = sys.stdin.readline

N,M = map(int, input().split())

A = list(map(int, input().split()))

Sol = 0

def f(x):
    M1=m=A[0]
    cnt = 1
    for i in range(1,N):
        M1 = max(M1,A[i])
        m = min(m,A[i])
        if (M1-m) > x:
            cnt = cnt + 1
            M1=m=A[i]
    return cnt<=M


start = 0
end = 10000
while start <= end:
    mid = (start + end) // 2
    if f(mid):
        end = mid - 1
        Sol = mid
    else:
        start = mid + 1
print(Sol)
