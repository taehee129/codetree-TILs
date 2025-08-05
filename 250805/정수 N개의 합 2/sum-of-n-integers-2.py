n,k = map(int,input().split())

nums = list(map(int,input().split()))

sums = [0]*n 

sums[0] = nums[0]
ans = sums[0]
for i in range(1,n) :
    sums[i] = sums[i-1]+nums[i] 

ans = sums[1] 
for i in range(k,n) : 
    ans = max(sums[i]-sums[i-k],ans)

print(ans)