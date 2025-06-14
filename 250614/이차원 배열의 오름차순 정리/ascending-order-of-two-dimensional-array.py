n= int(input())
MAX_K = min(10**2,n**2)

k= int(input())

def check(num) : 
    cnt = 0
    for i in range(1,n+1) :
        cnt += min(n, num//i)  
    
        if cnt >=k:
            return True
    return False 

import sys

left = 0 
right = n*n 
min_val = sys.maxsize
while left<=right : 
    mid = (left+right) //2 
    
    if check(mid) :
        right = mid -1 
        min_val = min(mid,min_val)
    else : 
        left = mid +1 

print(min_val)
