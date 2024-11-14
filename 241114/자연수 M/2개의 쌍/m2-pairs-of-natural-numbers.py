n = int(input())

lst = [
    list(map(int,input(split())))
    for _ in range(n)
]


m=0
for i in lst :
    m +=i[0]

maxVal =0
x = 0
y=n-1
for i in range(m/2) :

    if lst[x][0] <0 :
        x+=1
    if lst[y][0] <0 :
        y -=1
    lst[x][0] +=1
    lst[y][0] -=1

    maxVal = max(maxVal,lst[x][0] + lst[y][0])

print(maxVal)