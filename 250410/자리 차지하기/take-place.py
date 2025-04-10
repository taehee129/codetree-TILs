
from sortedcontainers import SortedSet

n,m = map(int,input().split())

nums =  list(map(int,input().split()))

chairs = SortedSet([i+1 for i in range(m)])

cnt = 0
for num in nums :  
    idx = chairs.bisect_right(num)
    if idx == 0 :
        break
    chairs.remove(chairs[idx-1])
    cnt +=1


print(cnt)

        
    
