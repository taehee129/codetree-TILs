import heapq 

hq= [] 

n= int(input())

for _ in range(n) : 
    num = int(input())
    if num != 0 :
        heapq.heappush(hq,(abs(num),num))
    else : 
        if hq :
            print(heapq.heappop(hq)[1])
        else :
            print(0)


        
