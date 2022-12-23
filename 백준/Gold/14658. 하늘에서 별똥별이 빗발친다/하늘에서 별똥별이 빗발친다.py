import sys

input = sys.stdin.readline

N,M,L,K = map(int, input().split())

C = 0
StarList = []
for x in range(K):
    StarList.append(list(map(int, input().split())))

for a in range(K): 
    for b in range(K):
        cnt = 0
        for c in range(K):
            if StarList[a][0] <= StarList[c][0] and StarList[c][0] <= StarList[a][0]+L and StarList[b][1] <= StarList[c][1] and StarList[c][1] <= StarList[b][1] + L:
                cnt = cnt + 1
        if C < cnt:
            C = cnt
print(K-C)
