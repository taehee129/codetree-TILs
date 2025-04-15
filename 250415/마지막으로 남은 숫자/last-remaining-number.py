import heapq as h 

n= int(input())

nums = list(map(int,input().split()))

hq = []

for num in nums :
    h.heappush(hq,-num)

while len(hq)>=2 :
    n1 = -h.heappop(hq)
    n2 = -h.heappop(hq)

    dif = n1-n2 
    if dif !=0 :
        h.heappush(hq,-dif)
    
    

if hq :
    print(-hq[0])
else :
    print(-1)

    