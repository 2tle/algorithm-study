import sys
input = sys.stdin.readline

bmod2 = 0
def query1(Pl, Pr):
    global bmod2
    bmod2  = (bmod2 + 1) % 2
def query2(Pl,Pr):
    global bmod2
    l = Pr - Pl + 1
    swapt = l // 2
    if swapt % 2 == 1:
        bmod2  = (bmod2 + 1) % 2
N,Q = map(int, input().split())
for x in range(Q):
    a,l,r = map(int, input().split())
    if a == 1:
        query1(l,r)
    else:
        query2(l,r)
    print(bmod2)
