import sys
input = sys.stdin.readline
import math

	
def f(i):
	return math.factorial(i)

tc = int(input())
for x in range(tc):
	m,n = map(int, input().split())

	 
	print(int(f(n)/(f(n-m) * f(m))))
