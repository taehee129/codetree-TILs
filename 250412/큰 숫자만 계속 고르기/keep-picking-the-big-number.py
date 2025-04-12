n,m = map(int,input().split())

import heapq

hq=  [] 

nums = list(map(int,input().split()))

for num in nums :
    heapq.heappush(hq,-num)

for _ in range(m) :
    num =  -heapq.heappop(hq)
    num -= 1
    heapq.heappush(hq,-num)

print(- hq[0])