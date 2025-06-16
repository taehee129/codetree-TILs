n,m= map(int,input().split())

lines = [tuple(map(int,input().split())) for _ in range(m)]


lines.sort(key=lambda x:x[0])



def check(val) :
    
    point= lines[0][0]
    cnt = 1
    for i,(a,b) in enumerate(lines) : 
        point = a if point < a else point       
        if point>b :
            continue 
        cnt += (b-point)//val +1 
        point = b+val 
        if cnt >=n :
            return True 
    
    return False 
               
    
left =1
right = 10**18
ans = 0
while left <=right : 
    mid = (left+right)//2 

    if check(mid) : 
        left = mid+1   
        ans =max(mid,ans)   
    else :
        right = mid-1 
    
print(ans)

        
