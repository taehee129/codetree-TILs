import heapq

hq = [] 

n = int(input())

for _ in range(n) :
    num = int(input())

    if num ==0 :
        if len(hq) == 0 :
            print(0)
        else :
            print(heapq.heappop(hq))
    else :
        heapq.heappush(hq,num)