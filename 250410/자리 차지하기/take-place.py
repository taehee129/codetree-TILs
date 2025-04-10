
from sortedcontainers import SortedSet

n,m = map(int,input().split())

nums =  list(map(int,input().split()))
nums.sort()

# 빈 자리이면서 앉을 수 있는 자리의 최댓값 

cnt = 0
end = len(nums)-1
for i in range(m,0,-1) : 
    if nums[end] >= i :
        cnt +=1 
        end -=1
       

print(cnt)

# nums의 최댓값이 i 보다 크거나 같으면 앉기 
# 작다면 ? i는 통과
    