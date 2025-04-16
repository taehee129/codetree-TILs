import heapq 

n,m,k= tuple(map(int,input().split()))

s1 = list(map(int,input().split()))
s2 = list(map(int,input().split()))


hq = []

for i in range(n) :
    for j in range(m) :
        heapq.heappush(hq,(s1[i]+s2[j]))


#print(hq)

for _ in range(k-1) :
    heapq.heappop(hq)

print(heapq.heappop(hq))