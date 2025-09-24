n=int(input())

nums = list(map(int,input().split()))

l = [0]*n 
r = [0]*n 

l[0] = nums[0]
r[n-1] = nums[n-1] 

for i in range(1,n) : 
    l[i] = max(l[i-1],nums[i])

for i in range(n-2,-1,-1) : 
    r[i] = max(r[i+1], nums[i])


ans = 0 

for i in range(2,n-2)  :
    ans = max(ans, l[i-2] + nums[i]+r[i+2]) 

print(ans)