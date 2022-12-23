import sys
from collections import Counter
input = sys.stdin.readline
N = int(input())
Nl = list(map(int, input().split()))
M = int(input())
Ml = list(map(int, input().split()))

c = Counter(Nl)

for i in range(M):
    print(c[Ml[i]], end=' ')