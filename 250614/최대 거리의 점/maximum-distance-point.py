n,m = map(int,input().split())

points = [int(input()) for _ in range(n)]


points.sort()

import sys
max_len = 0

for i in range(n) : 
    if i == n-1 :
        break
    
    max_len = max(max_len, abs(points[i]-points[i+1]))


def check(val) : 

    length = 0
    cnt = 1
    for i in range(1,n) : 
        length += (points[i]-points[i-1])
        if length >= val : 
            cnt +=1 
            length=0 
        
        if cnt == m : 
            return True 
    
    return False 


left = 2
right = 10**9 
max_val = 0

while left <=right : 
    mid = (left+right)//2

    if check(mid) : 
        max_val=max(max_val,mid)
        left = mid +1 
    else : 
        right = mid -1

print(max_val)
