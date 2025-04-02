n,k = map(int,input().split())

nums = list(map(int,input().split()))

def two(n,k) : 
    
    nums2 = nums[0:n]
    d = {} 
    ret = 0
    for i in range(n) : 
        num = nums2[i]   
        if k-num in d : 
            ret += d[k-num]
        
        if num in d :
            d[num] +=1 
        else :
            d[num] = 1 
    
    return ret 


asw = 0
for i in range(2,n) : 
    asw += two(i, k-nums[i])
    

print(asw)

