n = int(input())

lst = list(map(int,input().split()))

lst.sort()

sumVal = 0 

while len(lst) >1 :
    val = lst[0]+lst[1]
    sumVal += lst[0]+lst[1]
    lst = lst[2:]
    for i in range(len(lst)) :
        if val <= lst[i] :
            lst.insert(i,val)
            break
        if i == len(lst)-1 :
            lst.append(val)
    
print(sumVal)


