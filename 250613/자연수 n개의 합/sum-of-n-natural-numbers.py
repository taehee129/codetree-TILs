n= int(input())

left = 1 
right = n 


while left <= right : 
    mid = (left+right) //2 

    if mid *(mid+1)/2 <= n :
        break 
    else : 
        right -=1 
    
print(mid)
