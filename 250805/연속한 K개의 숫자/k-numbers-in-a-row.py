n,k,b = map(int,input().split())

nums = [True]*n 

for i in range(b) : 
    idx = int(input())-1
    nums[idx] = False


prefix = [0]*(n-k+1)

for i in range(k) : 
    if nums[i] is False : 
        prefix[0]+=1 


for i in range(1,n-k+1) : 
    prefix[i] = prefix[i-1] 

    if nums[i-1] is False : 
        prefix[i] -=1 
    
    if nums[i+k-1] is False : 
        prefix[i] +=1 

print(min(prefix))

