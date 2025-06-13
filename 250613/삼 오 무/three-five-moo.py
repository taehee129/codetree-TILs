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
        ans = mid   
        if ans%3==0 or ans%5==0 : 
            ans -=1
        break
    elif val > n : 
        right = mid -1 
    else : 
        left = mid +1

print(ans)