n,m = tuple(map(int,input().split()))


lst  = [
    list(map(int, input().split()))
    for _ in range(n)
]


lst.sort(key= lambda x : (x[1]/x[0]), reverse=True)

weight = [
    lst[i][0] 
    for i in range(len(lst))
]
x =0
sumVal=0
for _ in range(m) :

    if lst[x][0] == 0 :
        x +=1

    lst[x][0] -=1
    sumVal +=lst[x][1]/weight[x]
sumVal = "{:.3f}".format(sumVal)
print(sumVal)