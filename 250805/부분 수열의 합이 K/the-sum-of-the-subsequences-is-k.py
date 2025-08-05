n,k = map(int,input().split())

nums = list(map(int,input().split()))

sums = [0]*n 
sums[0] = nums[0]


for i in range(1,n) :
    sums[i] = sums[i-1]+nums[i] 
    
cnt = 0
for i in range(n) : 
    if sums[i] == k :
        cnt +=1 
    for j in range(n-1) : 
        if sums[i] - sums[j] == k : 
            cnt +=1 


print(cnt)