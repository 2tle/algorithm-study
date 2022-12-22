import sys
input = sys.stdin.readline
import heapq
N = int(input())
Query = []
for _ in range(N):
    Query.append(int(input()))
heapq.heapify(Query)
if Query.__len__() == 1:
    print(0)
else:
    result = 0
    while Query.__len__() != 1:
        first = heapq.heappop(Query)
        second = heapq.heappop(Query)
        sum = first + second
        result = result + sum
        heapq.heappush(Query,sum)
    print(result)