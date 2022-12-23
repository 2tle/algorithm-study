import sys
input = sys.stdin.readline

N = 1000 - int(input())
A=[500,100,50,10,5,1]
cnt = 0
for x in A:
    if x <= N:
       cnt = cnt + (N // x)
       N = N % x
print(cnt)
