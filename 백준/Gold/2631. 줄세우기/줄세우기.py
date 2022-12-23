import sys
input =sys.stdin.readline

def lowerBound(numList, find):
    l,r = 0,len(numList)
    while l < r:
        m = l+(r-l)//2
        if numList[m] < find:
            l = m + 1
        else: 
            r = m
    return r

def upperBound(numList, find):
    l,r = 0,len(numList)
    while l < r:
        m = l+(r-l)//2
        if numList[m] <= find:
            l = m + 1
        else:
            r = m
    return r


N = int(input())

A = []
for _ in range(N):
    A.append(int(input()))
K = []
K.append(A[0])

for x in range(1,N):
    if A[x] > K[len(K)-1]:
        K.append(A[x])
    else:
        K[lowerBound(K, A[x])] = A[x]
print(N - len(K))  