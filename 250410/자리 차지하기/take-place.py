
from sortedcontainers import SortedSet

n,m = map(int,input().split())

nums =  SortedSet(map(int,input().split()))

# 빈 자리이면서 앉을 수 있는 자리의 최댓값 

cnt = 0
for i in range(m,0,-1) : 
    if nums[-1] >= i :
        cnt +=1 
        nums.remove(nums[-1] )

print(cnt)

# nums의 최댓값이 i 보다 크거나 같으면 앉기 
# 작다면 ? i는 통과
    