n,k = map(int,input().split())

nums = list(map(int,input().split()))

d = {}

for num in nums : 
    if num in d :
        d[num]+=1 
    else : 
        d[num] =1 


sorted_items = sorted(d.items(), key= lambda item:(-item[1],-item[0]))

for i in range(k) :
    print(sorted_items[i][0], end= ' ')


