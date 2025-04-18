import heapq 

n,m,k= tuple(map(int,input().split()))

s1 = list(map(int,input().split()))
s2 = list(map(int,input().split()))


s1.sort()

import heapq 

hq = [] 

for i in range(m) : 
    heapq.heappush(hq,(s1[0]+s2[i],i,0)) 


for _ in range(k-1) : 
    _,i,j = heapq.heappop(hq)
    if j != n-1 :
        j+=1
        heapq.heappush(hq,(s1[j]+s2[i],i,j))

print(heapq.heappop(hq)[0])
    
