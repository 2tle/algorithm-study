import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
A.sort()
M = int(input())
K = list(map(int, input().split()))

#for x in K:

def b(answer):
    left = 0
    right = N-1
    while left <= right:
        mid = ( left + right ) //2
        if A[mid] == answer:
            return True

        if A[mid] < answer:
            left = mid + 1
        else:
            right = mid - 1

for x in K:
    if b(x):
        print(1)
    else:
        print(0)






