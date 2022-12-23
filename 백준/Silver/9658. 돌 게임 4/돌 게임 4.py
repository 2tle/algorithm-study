import sys
input = sys.stdin.readline

N= int(input())

arr = [False] * (N+1)
if(N!=1):
    arr[2] = True

for x in range(4, N+1):
    if (arr[x-1] == False or arr[x-3] ==False or arr[x-4] == False):
        arr[x] = True
print("CY" if not arr[N] else "SK")

