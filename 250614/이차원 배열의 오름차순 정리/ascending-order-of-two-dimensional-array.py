n= int(input())
MAX_K = min(10**2,n**2)

k= int(input())

def check(num) : 
    cnt = 0
    for i in range(n) : 
        for j in range(n) :
            val = (i+1)*(j+1)
            if num >= val :
                cnt +=1 

    return cnt 

import sys

left = 0 
right = n*n 
min_val = sys.maxsize

while left<=right : 
    mid = (left+right) //2 
    
    if check(mid) >= k :
        right = mid -1 
        min_val = min(mid,min_val)
    else : 
        left = mid +1 

print(min_val)
