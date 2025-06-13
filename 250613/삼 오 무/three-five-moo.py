MAX_NUM =10**10

n = int(input())

left = 1 
right= MAX_NUM 
ans = 0

while left <= right : 
    mid = (left+right)//2
    val = mid-(mid//3)-(mid//5)+(mid//15)
    #print(val, mid, left, right)
    if val == n : 
        if mid%3==0 or mid%5==0 : 
            right = mid -1          
        else : 
            ans = mid
            break
    elif val > n : 
        right = mid -1 
    else : 
        left = mid +1

print(ans)