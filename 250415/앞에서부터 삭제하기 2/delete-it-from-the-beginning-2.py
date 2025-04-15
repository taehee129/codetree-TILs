import heapq as h

n = int(input())
nums = list(map(int,input().split()))

import sys 

MIN_SIZE = 0
max_avg = MIN_SIZE

hq = []

min_num = [0]*n

for i in range(n-1,-1,-1) :
    
    h.heappush(hq,nums[i])
    min_num[i] = hq[0]


s = sum(nums) 

for k in range(0,n-2) : 
    s -= nums[k]
    max_avg = max(max_avg, (s-min_num[k+1])/(n-(k+2)))

print(f"{max_avg:.2f}")




    

    



    

        