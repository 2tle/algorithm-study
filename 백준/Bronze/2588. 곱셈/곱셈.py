X = int(input())
Y = str(input())[::-1]

for k in Y:
    print(X * int(k))

print(X * int(Y[::-1]))