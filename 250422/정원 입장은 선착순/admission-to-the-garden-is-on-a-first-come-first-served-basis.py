import heapq

n= int(input())


hq = [] 

for i in range(n) :
    s,e = tuple(map(int,input().split()))
    heapq.heappush(hq,(s,e,i))

gs,ge,gi = heapq.heappop(hq)

wq =[]

max_wt = 0
out_time = gs+ge
while hq :
    # print(hq)
    # print(wq)
    # print(gs,ge,gi)
    # print(max_wt)
    # print('*'*50)
    s,e,i = hq[0]

    if s < (gs+ge) : 
        heapq.heappush(wq,(i,s,e))
        heapq.heappop(hq)

    else :
        if wq :
            i,s,e = heapq.heappop(wq)
            max_wt = max(max_wt,out_time-s)
            out_time +=e
            gs,ge,gi = s,e,i
           
        else : 
            gs,ge,gi = heapq.heappop(hq)
            out_time +=e

# print('-'*50)
for _ in range(len(wq)) : 

    i,s,e = heapq.heappop(wq)
    max_wt = max(max_wt,out_time-s)
    out_time+=e
    gs,ge,gi = s,e,i


print(max_wt)


