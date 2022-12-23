#acmicpc.net 12865
#i hate py
import sys
input = sys.stdin.readline

N,K = map(int, input().split())
ddpp = [0]*(K+1)
for x in range(N):
    W,V = map(int, input().split())
    for y in range(K,W-1,-1):
        ddpp[y] = max(ddpp[y], ddpp[y-W] + V)
print(ddpp[K])
    
    