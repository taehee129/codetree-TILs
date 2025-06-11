n,m = map(int,input().split())

points = list(map(int,input().split()))

lines = [tuple(map(int,input().split())) for _ in range(m)]


def lower_bound(target) : 
    left = 0 
    right = n-1 
    min_idx = n 

    while left <= right :
        mid = (left+right) // 2 
        # print(left,right)
        # print("mid : " + str(mid))

        if points[mid] == target : 
         
            return mid
        elif points[mid] > target :
            min_idx = min(min_idx,mid)
            right = mid -1 
            # print("mid : " + str(mid))
            # print(min_idx)
        else : 
        
            left = mid +1 

    return min_idx 

def upper_bound(target) : 

    left = 0 
    right = n-1 
    max_idx = -1 

    while left <= right : 
        mid = (left+right) //2 

        if points[mid] == target :
            return mid 
        elif points[mid] > target : 
            right = mid -1 
        else : 
            left = mid +1 
            max_idx = max(max_idx,mid)
    
    return max_idx

for i in range(m) : 
    low = lower_bound(lines[i][0])
    up = upper_bound(lines[i][1])

    if low == n or up == -1 :
        print(0)
    else : 
        print(up-low+1)

