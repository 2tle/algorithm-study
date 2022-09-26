import sys
import math

input =sys.stdin.readline

N = int(input())
Convenience = []
for _ in range(N):
    Convenience.append(list(map(int, input().split())))

def distance(ax, bx, ay, by):
	return math.sqrt((ax-bx)**2 + (ay-by)**2)
x,y = 0,0
returnMaX = 10000000000
for x1,y1 in Convenience:
	tempMax = 0
	for x2,y2 in Convenience:
		MaX = distance(x1,x2,y1,y2)
		if tempMax < MaX:
			tempMax = MaX
	if returnMaX > tempMax:
		returnMaX = tempMax
		x,y = x1,y1
print(x,y)