n,t = map(int,input().split())
times = [int(input()) for _ in range(n)]

MAX_K = 10000

def check(k) :
    global times
    lst = times[0:k]
    idx = k
    time = 0
    while True : 
        #print(lst)
        min_time = min(lst)
        time += min_time       
        if time > t : 
            return False
        for i in range(k) : 
            lst[i] -= min_time
            if lst[i] == 0 :
                if idx == n :
                    break
                lst[i] = times[idx]
                idx+=1 
        
        if idx == n :
            # print(lst)
            # print(time)
            time += max(lst)            
            if time > t :
                return False 
            else : 
                return True

left =1 
right = n
ans = n

while left <= right : 
    mid = (left+right)//2 

    if check(mid) : 
        ans = min(ans,mid)
        right = mid -1
    else :
        left = mid +1

print(ans) 
        




        

    
