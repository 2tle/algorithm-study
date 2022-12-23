import sys
input = sys.stdin.readline
print = sys.stdout.write
N=int(input())
L = [ int(input()) for _ in range(N) ]

for x in sorted(L):
    print(str(x)+"\n")