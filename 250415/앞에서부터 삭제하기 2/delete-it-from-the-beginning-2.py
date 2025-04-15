import heapq as h

n = int(input())
nums = list(map(int,input().split()))

import sys 

MIN_SIZE = 0
max_avg = MIN_SIZE

hq =[]
for num in nums :
    h.heappush(hq,num)
    
s = sum(nums)
for k in range(0,n-2):
    num = nums[k]
    s -= num

    if num == hq[0] : 
        h.heappop(hq)
   
    max_avg = max(max_avg, (s-hq[0])/(n-(k+2)))
 
print(f"{max_avg:.2f}")

    

    
    


    

    



    

        