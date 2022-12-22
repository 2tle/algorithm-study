import sys
import math
input = sys.stdin.readline

N,P,Q = map(int, input().split())

dictionary = {}
dictionary[0] = 1

def f(n):
    if n in dictionary:
        return dictionary[n]
    else:
        dictionary[n] = f(math.trunc(n/P)) + f(math.trunc(n/Q))
        return dictionary[n]
print(f(N))