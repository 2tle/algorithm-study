a = int(input())
vo1 = [ i for i in range(1,a+1)]
res = []
while len(vo1) != 1:
    for x in range(1, len(vo1)+1):
        if x%2==1 and len(vo1)-1 >= x:
            res.append(vo1[x])
    vo1 = res
    res = []
print(vo1[0])