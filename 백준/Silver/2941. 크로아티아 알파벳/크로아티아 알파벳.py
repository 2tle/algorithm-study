import sys
C = ['c=','c-','dz=','d-','lj','nj','s=','z=']
K = sys.stdin.readline().rstrip()

for i in C:
    K = K.replace(i,'0')

print(len(K))
