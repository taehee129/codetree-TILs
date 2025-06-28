n = int(input())

MAX_N = 10**9

positions = [tuple(map(int,input().split())) for _ in range(n)]

positions.sort(key= lambda x : x[0])

def check(num) : 
    position =1 
    for idx,(x1,x2) in enumerate(positions) : 
        if idx == 0 :
            position = x1+num
            continue 
        pre_x1, pre_x2 = positions[idx-1][0], positions[idx-1][1]

        if position >= pre_x1 and position <= pre_x2 : 
            position = x1+num
            continue
        if position >= x1 and position <= x2 :
            position +=num          
        elif position > x2 : 
            return False 
        elif position < x1 : 
            position = x1+num 
        
        
    return True 

left = 1
right = MAX_N
max_num = 0

while left <= right : 
    mid = (left+right) //2 

    if check(mid) : 
        max_num = max(mid,max_num) 
        left =mid +1 
    else : 
        right = mid -1 
    
print(max_num)
        
        



