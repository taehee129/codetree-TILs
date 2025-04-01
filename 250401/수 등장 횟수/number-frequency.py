n,m = tuple(input().split())

lst = map(int,input().split())

d = {}

for num in lst :
    if num in d :
        d[num] = d[num] +1 
    else :
        d[num] = 1
    
lst = map(int,input().split())

for num in lst :
    if num in d :
        print(d[num], end = ' ')
    else :
        print(0)
