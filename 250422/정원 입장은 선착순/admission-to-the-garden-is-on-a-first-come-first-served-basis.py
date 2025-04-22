import heapq

n= int(input())


hq = [] 

for i in range(n) :
    s,e = tuple(map(int,input().split()))
    heapq.heappush(hq,(s,i,e))

gs,gi,ge = heapq.heappop(hq)

wq =[]

max_wt = 0
out_time = gs+ge
while hq :
    # print(hq)
    # print(wq)
    # print(gs,ge,gi)
    # print(max_wt)
    s,i,e = hq[0]

    if s < (gs+ge) : 
        heapq.heappush(wq,(i,s,e))
        heapq.heappop(hq)

    else :
        if wq :
            i,s,e = heapq.heappop(wq)
            max_wt = max(max_wt,out_time-s)
            out_time +=e
            gs,ge,gi = s,e,i
            #print(i,s,e,out_time)
           
        else : 
            gs,gi,ge = heapq.heappop(hq)
            out_time = gs+ge
            
    #print('*'*50)

#print('-'*50)
for _ in range(len(wq)) : 
    #print(wq)
    i,s,e = heapq.heappop(wq)
    #print(out_time,s)
    max_wt = max(max_wt,out_time-s)
    out_time+=e
    gs,ge,gi = s,e,i


print(max_wt)


