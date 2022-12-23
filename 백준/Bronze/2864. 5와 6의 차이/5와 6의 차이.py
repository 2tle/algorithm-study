from __future__ import print_function
import sys
input = sys.stdin.readline

X,Y = map(str,input().split())
XM,YM = X.replace('5','6'),Y.replace('5','6')
Xm, Ym = X.replace('6','5'), Y.replace('6','5')
print((int(Xm)+int(Ym)) , end=" ")
print((int(XM)+int(YM)))