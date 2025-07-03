n,k = map(int,input().split())

nums = list(map(int,input().split()))

d1 = {}
d2 = {}


cnt = 0

for num in nums : 

    diff = k-num 
    
    if diff in d2 :
        cnt += d2[diff]
    
    for key,v in d1.items() : 
        s = key +num 

        if s in d2 : 
            d2[s] += v 
        else :
            d2[s] =v         

    if num in d1 : 
        d1[num] +=1 
    else :
        d1[num] =1 

  

print(cnt)