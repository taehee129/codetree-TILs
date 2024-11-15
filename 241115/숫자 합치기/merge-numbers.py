n = int(input())

lst = list(map(int,input().split()))

lst.sort()

sumVal = 0 

while len(lst) >1 :
    val = lst[0]+lst[1]
    sumVal += lst[0]+lst[1]
    lst = lst[2:]
    lst.append(val)
    lst.sort()


print(sumVal)
