n,k = map(int,input().split())

nums = list(map(int,input().split()))

d = {}

for num in nums : 
    if num in d :
        d[num] +=1 
    else :
        d[num] = 1 


lst = []

for k,v in d.items() :
    lst.append((k,v))

lst.sort(key=lambda x:(x[1],x[0]), reverse=True)

for i in range(k) :
    print(lst[i][0], end =' ')