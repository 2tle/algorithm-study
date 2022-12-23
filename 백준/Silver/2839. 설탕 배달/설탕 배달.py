import sys
input = sys.stdin.readline

N = int(input())
cnt = 0

while N>=0:
    if N%5 ==0:
        cnt = cnt + N//5
        print(cnt)
        break
    else:
        N = N - 3
        cnt = cnt + 1
if(N<0):
    print(-1)
