import heapq

t= int(input())


for _ in range(t) :
    n = int(input())
    nums = list(map(int,input().split()))
    left_hq = []
    right_hq = []

    for idx, num in enumerate(nums) : 
        if not right_hq : 
            heapq.heappush(right_hq,num)
            print(num, end = ' ')
            #print('sdfsdf')
            continue
        
        mid_num = right_hq[0]

        if num >= mid_num : 
            heapq.heappush(right_hq,num)
        else : 
            heapq.heappush(left_hq,-num) 


        if (idx+1)%2 == 1 and len(right_hq) != len(left_hq)+1 :
            #left에 들어간 경우
            mid_num = -heapq.heappop(left_hq)
            heapq.heappush(right_hq,mid_num)
        elif (idx+1)%2 ==0 and len(right_hq) != len(left_hq) : 
            left_num = heapq.heappop(right_hq) 
            heapq.heappush(left_hq,-left_num)  

        if (idx+1)%2 == 1 :
            #print(t,idx,left_hq,right_hq)
            print(right_hq[0], end=' ')
      
    print() 
    
        


    



