n,m = map(int,input().split())

times = [int(input()) for _ in range(m)]


def check(val) :
    cnt = 0 
    for time in times : 
        cnt += val//time 
        if cnt >=n : 
            return True 
    
    return False 

import sys
MAX_SIZE = sys.maxsize 

left= 1 
right = MAX_SIZE 
ans = MAX_SIZE

while left <=right : 
    mid = (left+right)//2

    if check(mid) : 
        right = mid -1 
        ans = min(ans,mid)
    else : 
        left = mid +1

print(ans)
    