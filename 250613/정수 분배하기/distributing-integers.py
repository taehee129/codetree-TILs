K_MAX = 100000

n,m = map(int,input().split())

nums = [int(input()) for _ in range(n)]

def check(k) : 
    cnt = 0 

    for num in nums : 
        cnt += num//k 
    
    if cnt >= m :
        return True 
    else :
        return False

left = 0 
right = K_MAX 
k=0

while left <= right : 
    mid = (left + right)//2 

    if check(mid) : 
        left = mid +1 
        k = max(mid,k)
    else : 
        right = mid -1 

print(k)


    