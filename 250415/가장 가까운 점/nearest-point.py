n,m = map(int,input().split())

points = [tuple(map(int,input().split())) for _ in range(n)]

hq = []

import heapq 

for point in points :
    x,y = point
    heapq.heappush(hq,((x+y),x,y))


for _ in range(m) :  
    _,x,y = heapq.heappop(hq)
    x +=2
    y +=2
    heapq.heappush(hq, ((x+y),x,y))

print(hq[0][1],hq[0][2])