import sys

A,B,V = map(int,sys.stdin.readline().split())

D = (V - B) // (A - B) 
if(V - B) % (A - B) != 0:
    D = D + 1
print(D)
