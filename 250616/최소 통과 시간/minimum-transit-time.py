n,m = map(int,input().split())

times = [int(input()) for _ in range(m)]


def check(val) :
    cnt = 0 
    for time in times : 
        cnt += val//time 
        if cnt >=n : 
            return True 
    
    return False 


left= 1 
right = 10**9 
ans = right +1 

while left <=right : 
    mid = (left+right)//2

    if check(mid) : 
        right = mid -1 
        ans = min(ans,mid)
    else : 
        left = mid +1

print(ans)
    