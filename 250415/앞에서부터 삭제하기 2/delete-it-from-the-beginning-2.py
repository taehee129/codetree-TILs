import heapq as h

n = int(input())
nums = list(map(int,input().split()))

import sys 

MIN_SIZE = 0
max_avg = MIN_SIZE
for k in range(1,n-1) : 
    temp = [] 
    for i in range(k,n) :
        h.heappush(temp,nums[i])    

    h.heappop(temp)
    max_avg = max(max_avg, sum(temp)/len(temp))
    #print(k,temp,max_avg)
print(f"{max_avg:.2f}")


    

        